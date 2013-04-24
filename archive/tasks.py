import re
import mechanize

from pyquery import PyQuery as pq

from .models import Item


attrs = (
    'Issue:',
    'Category:',
    'Page:',
    'Center:',
    'State:',
    'Manufacturer:',
    'Origin:',
    'Tech Terms:',
    'Abstract:',

    'Additional Information:',
)

additional_attrs = (
    'Company:',  # optional, website
    'PDF chart:', # hmmm
)

LIST_URL = "http://spinoff.nasa.gov/spinoff/spinsearch?BOOL=AND&ALLFIELDS=&CENTER=&BOOLM=AND&MANUFACT=&STATE=&CATEGORY=&ISSUE=&Spinsort=ISSUED"


def find_attr(attr, content, attrs=attrs):
    "Really ugly code for finding a string between two attrs in spinoff content"
    try:
        attr_index = content.index(attr)
    except ValueError:
        "attr is not in content"
        return None

    try:
        neighbor = attrs[attrs.index(attr) + 1]
    except IndexError, ValueError:
        "This means it's the last item in the content text"
        neighbor = None

    if neighbor:
        try:
            return content[(attr_index + len(attr)):content.index(neighbor)].strip()
        except Exception:
            pass
    try:
        return content[attr_index + len(attr):].strip()
    except Exception:
        return None  # yeah....messy data



def scrape_spinoffs(force=False):
    "Iterate through all spinoff links, parse the content and save archive.Item"
    br = mechanize.Browser()
    br.open(LIST_URL)
    links = br.links(url_regex="/spinoff/spinitem\?title=(.*)")

    for link in list(links):
        source_url = link.absolute_url

        if not force:
            if Item.objects.filter(source_url=source_url).exists():
                print('Skipping "{}"...'.format(source_url))
                continue

        br.follow_link(link)
        html = br.response().read()
        doc = pq(html)
        title = doc('.itemtitle').text()

        # turns out its easiest to just read the text_content for the
        # whole table in and parse it as a string.
        content = doc('#MCBlock table')[0].text_content()

        issue = find_attr('Issue:', content)
        if not issue:
            issue = 0
        category = find_attr('Category:', content)
        page = find_attr('Page:', content)
        center = find_attr('Center:', content)
        state = find_attr('State:', content)
        manufacturer = find_attr('Manufacturer:', content)
        origin = find_attr('Origin:', content)
        tech_terms = find_attr('Tech Terms:', content)

        abstract = find_attr('Abstract:', content)
        additional = find_attr('Additional Information:', content)

        abstract = (re
                    .sub(r'\xc2\xa0', '', abstract.encode('utf-8'))
                    .replace('+ Go To Full Article', '')
                    .strip())

        company = find_attr('Company:', additional, attrs=additional_attrs)
        pdf_chart = find_attr('PDF chart:', additional, attrs=additional_attrs)


        Item.objects.create(
            title=title,
            year=issue,
            center=center,
            page=page,
            manufacturer=manufacturer,
            origin=origin,
            tech_terms=tech_terms,
            abstract=abstract,
            full_article_url=pdf_chart,
            company=company,
            category=category,
            state=state,
            source_url=source_url,
            # manufacturer_url=
            # full_article_url
            )
        print Item


def find_dupes():
    br = mechanize.Browser()
    br.open(LIST_URL)
    links = br.links(url_regex="/spinoff/spinitem\?title=(.*)")

    urls = set()
    dupes = list()
    for link in list(links):
        url = link.absolute_url
        if url in urls:
            dupes.append(url)
        else:
            urls.add(url)

    print "{} dupes found!".format(len(dupes))
    print "\n".join(sorted(dupes))
