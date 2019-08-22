from django.contrib import admin

from .models import Post, Vote

class PostAdmin(admin.ModelAdmin):
    list_display = ('description', 'parent')


admin.site.register(Post, PostAdmin)
