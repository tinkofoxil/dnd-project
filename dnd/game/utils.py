from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Game, GameSession, GameUser, PlayerAction
from django.utils import timezone


def start_game_session(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    if game.status != 'created':
        return JsonResponse({'error': 'Игра уже началась или завершена.'}, status=400)

    game.status = 'started'
    game.start_time = timezone.now()
    game.save()

    session = GameSession.objects.create(game=game, current_round=1)
    return JsonResponse({'message': 'Игра началась.', 'session_id': session.id})


def end_game_session(request, session_id):
    session = get_object_or_404(GameSession, pk=session_id)
    session.end_time = timezone.now()
    session.save()

    game = session.game
    game.status = 'finished'
    game.finish_time = timezone.now()
    game.save()

    return JsonResponse({'message': 'Игра завершена.'})
