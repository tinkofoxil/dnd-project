from django.contrib import admin

from .models import Game


class GameAdmin(admin.ModelAdmin):
    fields = ['name', 'users']
    filter_horizontal = ('users',)


admin.site.register(Game, GameAdmin)
