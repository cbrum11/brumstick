from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Post

# Apply summernote to all TextField in model.
class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Post, PostAdmin)
