from django.contrib import admin

from .models import Homework


# Register your models here.
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ["title", "subject", "due", "is_finished"]
    list_filter = ["subject", "due", "is_finished"]
    search_fields = ["title", "subject", "description"]
    list_editable = ["is_finished"]
    list_per_page = 10
    date_hierarchy = "due"


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user=request.user)
    # Override save_model to set the user field
    def save_model(self, request, obj, form, change):
        if not change:  # Only set user during the first save
            obj.user = request.user
        super().save_model(request, obj, form, change)
    
admin.site.register(Homework, HomeworkAdmin)