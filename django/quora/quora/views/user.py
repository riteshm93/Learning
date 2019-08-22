from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('quora:questions'))
        else:
            return render(request, 'quora/index.html')
    else:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('quora:questions'))
        else:
            return HttpResponse("Login Error.")


def signup(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('quora:questions'))
        else:
            return render(request, 'quora/index.html')
    else:
        user = User.objects.create_user(
                request.POST['username'],
                request.POST['email'],
                request.POST['password'],
                first_name = request.POST['firstname'],
                last_name = request.POST['lastname'])
        user.save()
        if user.is_authenticated():
            auth_login(request, user)
            return HttpResponseRedirect(reverse('quora:questions'))
        else:
            return HttpResponse("Signup Error.")


@login_required(login_url='/quora/')
def logout(request):
    if request.user.is_authenticated():
        auth_logout(request)
    return HttpResponseRedirect(reverse('quora:index'))

