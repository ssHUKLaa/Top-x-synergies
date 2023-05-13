from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .withriotapi import getChallengerPlayers, getPlayer, getMatches, getProfilePicture
import requests

def index(request):
    return HttpResponse("N/A")

def players_by_api(request, player):
    if request.method == 'POST':
        summoner_name = request.POST['inp_number']
        #players:player refers to topplayers/urls.py where app_name=players
        return redirect('players:player',player=summoner_name)
    if (getPlayer(player)==False):
        return HttpResponse(f'not a person')
    contestant=(getPlayer(player))
    tes=(getProfilePicture(contestant))
    playername={"player": contestant.get('name'), "profpic": tes}
    return render(request, 'topplayers/player.html',playername)
# Create your views here.