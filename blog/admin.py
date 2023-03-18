from django.contrib import admin
from blog.models import Post,Category
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'status', 'counted_views',
                    'published_date', 'updated_date')
    list_filter = ('status', 'author')
    search_fields = ['title', 'content',]

admin.site.register(Category)
admin.site.register(Post, PostAdmin)

