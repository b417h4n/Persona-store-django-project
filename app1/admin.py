from django.contrib import admin
from app1.models import Toy
from app1.models import Orders


class ImageAdmin(admin.ModelAdmin):
    list_display = ["name", "desc", "price", "photo"]


admin.site.register(Orders)
admin.site.register(Toy, ImageAdmin)
