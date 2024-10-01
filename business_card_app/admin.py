from django.contrib import admin
from .models import (
    BiographyEvent,
    Contact,
    Footer,
    Gallery1,
    Gallery2,
    Gallery3,
    Gallery4,
    Gallery5,
    GalleryImage,
)


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ("id", "div_text", "p1_text", "p2_text", "p3_text")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "number", "comment"]


@admin.register(Gallery1)
class GalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(Gallery2)
class GalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(Gallery3)
class GalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(Gallery4)
class GalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(Gallery5)
class GalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    pass


@admin.register(BiographyEvent)
class BiographyEventAdmin(admin.ModelAdmin):
    list_display = (
        "year",
        "text",
        "image",
    )  # Поля, которые будут отображаться в списке
    search_fields = ("year", "text")  # Поля, по которым можно искать
    list_filter = ("year",)  # Фильтрация по году
