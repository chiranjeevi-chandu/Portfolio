from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "mobile", "subject", "message", "created_at", "seen_at"]
    search_fields = ("name", "email", "mobile", "subject", "message", "created_at", "seen_at")


admin.site.register(Contact, ContactAdmin)

