from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin

class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    readonly_fields = ['image_preview']

    def image_preview(self, place):
        return format_html("<img src='{url}' width=200 max-height=200 />".format(
            url = place.img.url
        )
    )
    model = Image

class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Place, PlaceAdmin)
admin.site.register(Image)