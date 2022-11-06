from django.contrib import admin
from .models import News, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
    search_fields = ('title',)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at',
                    'updated_at', 'is_published', 'category')
    list_display_links = ('id', 'title', 'category')
    search_fields = ('title', 'content', 'category')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
