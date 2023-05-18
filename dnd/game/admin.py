from django.contrib import admin

from .models import Game, GameUser


class GameAdmin(admin.ModelAdmin):
    fields = ['name']


class GameUserAdmin(admin.ModelAdmin):
    fields = ['user', 'game']


admin.site.register(Game, GameAdmin)
admin.site.register(GameUser, GameUserAdmin)
