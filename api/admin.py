from django.contrib import admin
from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    """Admin interface for managing user accounts."""

    list_display = ('full_name', 'telegram_id', 'phone_number', 'created_at')
    search_fields = ('first_name', 'last_name', 'telegram_id', 'username')
    readonly_fields = ('telegram_id', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')

    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'image')
        }),
        ('Contact Details', {
            'fields': ('phone_number', 'telegram_id', 'username')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
