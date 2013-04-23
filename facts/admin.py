from django.core.urlresolvers import reverse
from django.contrib import admin

from .models import Fact
from .forms import FactForm

def set_level_one(modeladmin, request, queryset):
    queryset.update(level=1)

set_level_one.short_description = "Set Level 1"


def set_level_two(modeladmin, request, queryset):
    queryset.update(level=2)

set_level_two.short_description = "Set Level 2"


def set_level_three(modeladmin, request, queryset):
    queryset.update(level=3)

set_level_three.short_description = "Set Level 3"



class FactAdmin(admin.ModelAdmin):
    model = Fact
    form = FactForm
    list_display = ('fact', 'spinoff_link', 'level',  )
    list_filter = ('level', )
    actions = (set_level_one, set_level_two, set_level_three, )
    fieldsets = (
        (None, {
            'fields': ('spinoff', 'fact', 'level', 'active', )
        }),
        ('Quiz', {
            'fields': ('question', 'answer_text', 'answer_image', )
        }),
    )

    def spinoff_link(self, obj):
        url = reverse('admin:archive_item_change', args=[obj.spinoff_id])
        return "<a href='{}'>{}</a>".format(url, obj.spinoff)
    spinoff_link.allow_tags = True

admin.site.register(Fact, FactAdmin)
