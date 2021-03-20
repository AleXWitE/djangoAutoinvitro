from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import News, Notification, Sale, SaleItem, Car, Forum, Posts, Events

# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date', 'author', 'visible')
    list_display_links = ('id', 'title', 'author')
    search_fields = ('id', 'title', 'description', 'date', 'author', 'visible')
    list_editable = ('visible',)
    list_filter = ('visible', 'author', 'date')


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date', 'author', 'visible')
    list_display_links = ('id', 'title', 'author')
    search_fields = ('id', 'title', 'description', 'date', 'author', 'visible')
    list_editable = ('visible',)
    list_filter = ('visible', 'author', 'date')


class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date', 'seller', 'visible', 'cost')
    list_display_links = ('id', 'title', 'seller')
    search_fields = ('id', 'title', 'description', 'date', 'seller', 'visible')
    list_editable = ('visible',)
    list_filter = ('visible', 'seller', 'cost')


class SaleItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'seller', 'visible', 'cost', 'photo')
    list_display_links = ('id', 'title', 'seller')
    search_fields = ('id', 'title', 'description', 'seller', 'visible')
    list_editable = ('visible',)
    list_filter = ('visible', 'seller', 'cost')


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date', 'author', 'visible', 'cost', 'mileage')
    list_display_links = ('id', 'title', 'author')
    search_fields = ('id', 'title', 'description', 'date', 'author', 'visible')
    list_editable = ('visible',)
    list_filter = ('visible', 'author', 'cost')


class ForumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'numPosts', 'curator')
    list_display_links = ('id', 'title', 'curator')
    search_fields = ('id', 'title', 'description', 'curator')
    list_filter = ('curator',)


class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'forum', 'title', 'description', 'date', 'author')
    list_display_links = ('id', 'forum', 'author')
    search_fields = ('id', 'forum', 'description', 'author')
    list_filter = ('author',)


class EventsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'date')


admin.site.register(News, NewsAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(SaleItem, SaleItemAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Forum, ForumAdmin)
admin.site.register(Posts, PostsAdmin)
admin.site.register(Events, EventsAdmin)
