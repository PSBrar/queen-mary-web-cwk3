from django.shortcuts import render
from django.http import HttpResponse
from users.models import Hobby
from django.template import RequestContext

# Create your views here.

def profile(request):
    return render(request, 'hobbies/profile.html', {'title': 'Profile'})

def hobbies(request):
    #single_car = Hobby.objects.get(pk=car_id)
    UserHobbies = Hobby.objects.all()
    return render(request, 'hobbies/hobbies.html',{
        'title': 'Hobbies',
        "hobby":  UserHobbies,
        })