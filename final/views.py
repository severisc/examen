
from django.shortcuts import render
from django.http import HttpResponse
from .models import User



def users(request):
    persoane = User.objects.all()
    return render(request, 'final/users.html', {'persoane':persoane})