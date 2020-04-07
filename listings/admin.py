from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'realtor')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
admin.site.register(Listing, ListingAdmin)
