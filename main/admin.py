from django.contrib import admin
from django.utils.safestring import mark_safe
from import_export import fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources

from .models import User, Goods, Tattoo, Piercing




@admin.register(Goods)
class GoodsAdmin(ImportExportActionModelAdmin):
    resource_class = Goods
    list_display = ("name", "get_image")
    readonly_fields = ("get_image", )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="220" height="250"')

    get_image.short_descriprion = "Изображение"

admin.site.register(User)

admin.site.register(Tattoo)
admin.site.register(Piercing)


