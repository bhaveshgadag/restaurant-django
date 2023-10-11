from django.contrib import admin
from .models import Item


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('meal', 'description', 'status')
    list_filter = ('status',)


admin.site.register(Item, MenuItemAdmin)
