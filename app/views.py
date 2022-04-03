from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import User

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def login(request):
    result = User.objects.filter(username=request.POST['username'], password = request.POST['password'])
    if len(result) >= 1:
        return HttpResponseRedirect(reverse('app:berhasil'))
    else:
        return HttpResponseRedirect(reverse('index'))

def inside(request):
    return render(request, 'app/inside.html')