from django.contrib import admin

from contact.models import ContactModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    search_fields = ['name', 'message']
    list_display = ['name', 'email', 'created_at']
    list_filter = ['created_at']
