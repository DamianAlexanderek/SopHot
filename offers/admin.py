from django.contrib import admin
from .models import Category, Offers


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Offers)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'adres',
                    'image', 'bonus', 'available', 'description', 'created']
    list_filter = ['name', 'bonus', 'available']
    list_editable = ['bonus', 'available']
    prepopulated_fields = {'slug': ('name', )}
