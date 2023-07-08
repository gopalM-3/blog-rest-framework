from django.contrib import admin
from . import models


@admin.register(models.Blog)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'status', 'slug')
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(models.Category)
