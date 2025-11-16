from django.contrib import admin

from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['title', 'desc']
    list_display_links = ['title', 'status']
    list_per_page = 5
    # prepopulated_fields = {'desc':('title',)}
    