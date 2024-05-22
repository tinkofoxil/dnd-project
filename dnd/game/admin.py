from django.contrib import admin

from .models import Game, GameUser, GameSession, Invitation, PlayerAction


class GameUserInline(admin.TabularInline):
    model = GameUser
    extra = 1


class GameAdmin(admin.ModelAdmin):
    inlines = [GameUserInline]
    fields = ['name', 'status']
    search_fields = ('name',)
    list_filter = ('status',)


class GameUserAdmin(admin.ModelAdmin):
    fields = ['user', 'game', 'profile']


class GameSessionAdmin(admin.ModelAdmin):
    fields = ['game', 'current_round',]


class InvitationAdmin(admin.ModelAdmin):
    fields = ['sender', 'recipient', 'game']


class PlayerActionAdmin(admin.ModelAdmin):
    fields = ['session', 'player', 'action_type', 'description',]


admin.site.register(Game, GameAdmin)
admin.site.register(GameUser, GameUserAdmin)
admin.site.register(GameSession, GameSessionAdmin)
admin.site.register(Invitation, InvitationAdmin)
admin.site.register(PlayerAction, PlayerActionAdmin)
