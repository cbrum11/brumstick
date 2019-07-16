from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Projects

# Apply summernote to all TextField in model.
class ProjectsAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Projects, ProjectsAdmin)
