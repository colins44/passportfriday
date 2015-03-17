from django.contrib import admin
from .models import WeekendItem, Weekend
from genericadmin.admin import GenericAdminModelAdmin, GenericTabularInline


class TaggedItemInline(GenericTabularInline):
    content_type_whitelist = ('flights/routes', 'accommodation/accommodation')
    model = WeekendItem
    fields = ['parent_content_type','parent_object_id']
    ct_field = 'content_type'
    ct_fk_field = 'object_id'
    extra = 3

class WeekendAdmin(GenericAdminModelAdmin):
    inlines = [TaggedItemInline, ]

admin.site.register(Weekend, WeekendAdmin)