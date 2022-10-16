from django.contrib import admin
from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'time_create')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}

class AccidentsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ['title']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(News, NewsAdmin)
admin.site.register(Accidents, AccidentsAdmin)
admin.site.register(Category,  CategoryAdmin)



# Register your models here.
