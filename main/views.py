from django.shortcuts import render
from .models import *


def get_users(request):
    users = StepUsers.objects.all()

    context = {
        'users': users
    }
    return render(request, 'index.html', context)