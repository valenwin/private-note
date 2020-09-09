from django.contrib import admin
from ..core.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_filter = ('is_viewed',)
    search_fields = ('text', 'is_viewed')
    list_per_page = 20
