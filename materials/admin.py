from django.contrib import admin
from .models import Material

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'order', 'is_published')
    list_editable = ('order', 'is_published')

