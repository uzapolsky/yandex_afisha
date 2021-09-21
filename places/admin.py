from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin

class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    readonly_fields = ['image_preview']

    def image_preview(self, place):
        return format_html(
            "<img src='{url}' style='width:200px; max-height:200px' />",
            url = place.img.url
        )
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Image)