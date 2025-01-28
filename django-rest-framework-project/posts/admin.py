from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created_at']
    search_fields = ['title', 'content']
    list_filter = ['created_at']
    date_hierarchy = 'created_at'
    ordering = ['created_at']
    list_per_page = 10
    list_max_show_all = 100
    list_editable = ['content']
    fieldsets = [
        ('Post Information', {'fields': ['title', 'content', 'created_at']}),
    ]
    add_fieldsets = [
        ('Post Information', {'fields': ['title', 'content', 'created_at']}),
    ]
    readonly_fields = ['created_at']
    actions_on_bottom = True
    actions_on_top = False
    actions_selection_counter = False
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True
    save_as = True
    save_on_top = True