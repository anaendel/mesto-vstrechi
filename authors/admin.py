from django.contrib import admin

from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_year', 'death_year', 'is_published')
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)