from django.contrib import admin

from .models import Profile, Inventory, Item


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'user', 'created_at')


class InventoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'character')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Item, ItemAdmin)
