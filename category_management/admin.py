from django.contrib import admin
from category_management.models import Category,Blog,FAQ,News
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','type','published')
    list_filter = ['published','type']

admin.site.register(Category,CategoryAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category','short_description', 'description','image','status','meta_title','meta_description','meta_keyword','og_title','og_description','og_url','canonical_url')
    list_filter = ['status','title']
admin.site.register(Blog,BlogAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'short_description', 'description','image','status','meta_title','meta_description','meta_keyword','og_title','og_description','og_url','canonical_url')
    list_filter = ['status','title']
admin.site.register(News,NewsAdmin)


class FAQAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'short_description', 'description','image','status','meta_title','meta_description','meta_keyword','og_title','og_description','og_url','canonical_url')
    list_filter = ['status','title']
admin.site.register(FAQ,FAQAdmin)

