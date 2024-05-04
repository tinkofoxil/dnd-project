from django.contrib import admin

from .models import CustomUser, Friendship


class CustomUserAdmin(admin.ModelAdmin):
    fields = ['username', 'email', 'password', 'avatar']
    search_fields = ('username',)


class FriendshipAdmin(admin.ModelAdmin):
    fields = ['user', 'friend']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Friendship, FriendshipAdmin)
