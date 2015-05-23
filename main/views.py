from django.shortcuts import render
from django.contrib.auth import login, logout
from .models import *
from datetime import *


def index(request):
    return render(request, 'index.html')


def profile(request, user_id):
    users = StepUsers.objects.all().order_by('-steps')[:10]
    theUser = StepUsers.objects.get(stepUser__id=user_id)
    steps = StepUsersHistory.objects.all()
    fats = StepUsers.objects.all().order_by('steps')[:10]

    month = date.today() - timedelta(days=30)
    week = date.today() - timedelta(days=7)
    today = date.today()

    # stepsmonth = StepUsersHistory.objects.filter(user__stepUser__id=user_id).filter(date__startswith=date.today).filter(date__endswith=month)
    # stepsmonth = StepUsersHistory.objects.filter(user__stepUser__id=user_id).filter(date__range=(today, month))
    stepsmonth = StepUsersHistory.objects.filter(date__range=(today, month))
    print stepsmonth
    stepmonth = 0
    for step in stepsmonth:
        stepmonth += step.steps

    stepsweek = StepUsersHistory.objects.filter(user__stepUser__id=user_id).filter(date__startswith=date.today).filter(date__endswith=week)
    stepweek = 0
    for step in stepsweek:
        stepweek += step.steps

    stepstoday = StepUsersHistory.objects.filter(user__stepUser__id=user_id).filter(date=today)
    steptoday = 0
    for step in stepstoday:
        steptoday += step.steps

    context = {
        'theUser': theUser,
        'users': users,
        'steps': steps,
        'fats': fats,
        'stepmonth': stepmonth,
        'stepweek': stepweek,
        'steptoday': steptoday,
        'stepsmonth': stepsmonth
    }
    return render(request, 'profile/profile.html', context)


def profile_edit(request):
    return render(request, 'profile/profile-edit.html')


def profiles(request):
    users = StepUsers.objects.all()
    steps = StepUsersHistory.objects.all()
    context = {
        'users': users,
        'steps': steps
    }
    return render(request, 'profile/profiles.html', context)


def login_view(request):
    pass


def logout_view(request):
    logout(request)