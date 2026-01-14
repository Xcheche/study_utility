from django.contrib import admin

from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "completed", "user")
    # list_filter = ("completed",)
    search_fields = ("title",)
    ordering = ("title",)

# Register your models here.

admin.site.register(Note)