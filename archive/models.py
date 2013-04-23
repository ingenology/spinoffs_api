from django.db import models


class Item(models.Model):
    source_url = models.URLField()
    year = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    center = models.CharField(max_length=255, blank=True, null=True)
    page = models.CharField(max_length=255, blank=True, null=True)
    center = models.CharField(max_length=255, blank=True, null=True)
    manufacturer = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    manufacturer_url = models.URLField(blank=True, null=True)
    origin = models.CharField(max_length=255, blank=True, null=True)
    tech_terms = models.CharField(max_length=255, blank=True, null=True)
    abstract = models.TextField(blank=True, null=True)
    full_article_url = models.URLField(blank=True, null=True)
    pdf_chart_url = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.title
