from django.shortcuts import render, redirect
from .models import Game
from .forms import GameForm, UserRegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout


def game_list(request):
	games = Game.objects.all()
	context = {
		"games": games,
	}
	return render(request, 'game_list.html', context)

def game_detail(request, Game_id):
	context = {
		"details": Game.objects.get(id=Game_id),
	}
	return render(request, 'game_detail.html', context)

def create_game(request):
	form = GameForm()
	if request.method == "POST":
		form = GameForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("game_list")
	context = {
		"form": form,
	}
	return render(request, 'game_create.html', context)

def update_game(request, Game_id):
	game_obj = Game.objects.get(id=Game_id)
	form = GameForm(instance=game_obj)
	if request.method == "POST":
		form = GameForm(request.POST, instance=game_obj)
		if form.is_valid():
			form.save()
			return redirect("game_detail", Game_id)
	context = {
		"form": form,
		"obj": game_obj,
	}
	return render(request, 'update_game.html', context)

def game_delete(request, Game_id):
	Game.objects.get(id=Game_id).delete()
	return redirect("game_list")

def user_register(request):
	form = UserRegisterForm()
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			# user = form.save(commit=False)
			my_user = user.username
			my_password = user.password
			user.set_password(user.password)
			user.save()
			
			login(request, user)
			return redirect("game_list")
	context = {
		"form": form
	}
	return render(request, 'register.html', context)


def user_login(request):
	form = LoginForm()
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			my_username = form.cleaned_data['username']
			my_password = form.cleaned_data['password']
			auth_user = authenticate(username=my_username, password=my_password)
			if auth_user is not None:
				login(request, auth_user)
				return redirect("game_list")
	context = {
		"form": form
	}
	return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    return redirect("game_list")
