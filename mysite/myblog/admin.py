from django.contrib import admin
from myblog.models import Post
from myblog.models import Category


class CategoryInline(admin.StackedInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'author']
    ordering = ['created_date']
    inlines = [CategoryInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    ordering = ['posts']
    exclude = ('posts',)



admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
