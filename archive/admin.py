from django.contrib import admin

from .models import Item
from .forms import ItemForm

from facts.models import Fact
from facts.forms import FactForm


class FactInline(admin.StackedInline):
    model = Fact
    form = FactForm
    extra = 0
    fieldsets = (
        (None, {
            'fields': ('spinoff', 'fact', 'image', 'level', 'active', )
        }),
        ('Quiz', {
            'fields': ('question', 'answer_text', 'answer_image', )
        }),
    )


class ItemFactFilter(admin.SimpleListFilter):
    title = 'Facts'
    parameter_name = 'has_fact'

    def lookups(self, request, model_admin):
        return (
            ('True', 'Has facts.'),
            ('False', 'Needs facts.'),
        )

    def queryset(self, request, queryset):
        "There has to be a better way to do this"
        if self.value() == 'True':
            return queryset.filter(pk__in=Fact.objects.values_list('spinoff', flat=True))
        elif self.value() == 'False':
            return queryset.exclude(pk__in=Fact.objects.values_list('spinoff', flat=True))


class ItemModelAdmin(admin.ModelAdmin):
    form = ItemForm
    list_display = ('title', 'year', 'category', 'fact_count', )
    list_filter = (ItemFactFilter, 'category', 'year', )
    search_fields = ('title', 'category', 'tech_terms', 'abstract', 'manufacturer', )
    model = Item
    readonly_fields = ('tech_terms', 'origin', )
    inlines = (FactInline, )
    fieldsets = (
        (None, {
            'fields': ('title', 'source_url', 'abstract', )
        }),
        ('Metadata', {
            'classes': ('collapse', ),
            'fields': (
                'year', 'category', 'manufacturer', 'origin',
                'tech_terms', 'full_article_url', 'pdf_chart_url',
            )
        }),
    )

    def fact_count(self, obj):
        return obj.fact_set.count()

admin.site.register(Item, ItemModelAdmin)
