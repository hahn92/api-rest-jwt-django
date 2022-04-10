from django.contrib import admin

# Models
from .models import Tasks

@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    """
    Vista Tasks en administrador
    """
    list_display = ('pk', 'title', 'tasks_author', 'tasks_state', 'created', 'modified')
    list_display_links = ('pk', 'title',)

    search_fields = (
        'title',
        'description',
        'tasks_author__username',
    )

    list_filter = (
        'tasks_state',
        'is_active',
        'created',
        'modified',
    )

    fieldsets = (
        ('Datos basicos', {
            'fields': (
                ( 'title', 'tasks_author', 'is_active', 'tasks_state',), 
                'description', 
            ),
        }),
        ('Metadatos', {
            'fields': ('created', 'modified',),
        })
    )

    autocomplete_fields = ['tasks_author']
    readonly_fields = ('created', 'modified',)
