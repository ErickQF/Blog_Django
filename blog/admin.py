from django.contrib import admin
from blog.models import Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'category')
    search_fields = ['id', 'name', 'status']
    list_filter = ['category', 'status']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

