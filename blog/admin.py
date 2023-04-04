from django.contrib import admin
from blog.models import Post
from blog.models import Category


class PostAdmin(admin.ModelAdmin):
    fieldsets=[
        ('Relation', {'fields':['category']}),
        (
        'General Information',
        {
        'fields': [
        'date_published', 'post', 'image', 'status'
        ]
        }
        ),
    ]
admin.site.register(Post, PostAdmin)
admin.site.register(Category)