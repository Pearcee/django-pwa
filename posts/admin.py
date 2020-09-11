from django.contrib import admin
from .models import feed

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(feed)