from django.contrib import admin

from .models import Game


class GameAdmin(admin.ModelAdmin):
    fields = ['name', 'character']


admin.site.register(Game, GameAdmin)
