from django.http import HttpResponseRedirect, HttpResponse
from .models import Idee, Votant
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404

def home(request):
    
    return render(request, "main/home.html")

from django.urls import reverse_lazy, reverse


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Si le formulaire est valide on crée l'utilisateur
            form.save()
            # Et ensuite on le log
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse_lazy('home'))
        
    else:
        form = UserCreationForm()

    return render(request, 'main/signup.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'main/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


# views pour afficher toutes les idées
def afficher_idees(request):
    idees = Idee.objects.all()
    return render(request, 'main/idees.html', {'idees': idees})


#views pour ajouter une nouvelle idée*
from .forms import IdeeForm

def ajouter_idee(request):
    if request.method == 'POST':
        form = IdeeForm(request.POST)
        if form.is_valid():
            idee = form.save(commit=False)
            idee.auteur = request.user
            idee.save()
            return redirect('afficher_idees')
    else:
        form = IdeeForm()
    return render(request, 'main/ajouter_idee.html', {'form': form})



