from django.http import JsonResponse
from django.http.response import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Person, Hobby
from django.contrib.auth.decorators import login_required
import os



def person_api(request, slug):
    '''
        API entry point for each country
    '''
    #if request.method == "POST":
        #    

    if request.method == "PUT":
        #person = get_object_or_404(Person, userID=slug)
        body = json.loads(request.body)
        pUserId = body["userID"]
        pImage = body["image"]
        pCity = body["city"]
        pEmail = body["email"]
        pDOB = body["dob"]
        #pHobbies =
        person.save()
        return JsonResponse({})

    if request.method == "GET":
        #body = json.loads(request.body.decode("utf-8"))
        #person = get_object_or_404(Person, userID=slug)
        try:
            #print(slug)
            #queryset = Person.objects.filter(userID=slug)
            #URL = Person.objects.filter(userID=slug)
           # URL = URL.image
            personEntity = Person.objects.get(userID=slug)
            personHobbies = personEntity.hobbies.all()
            return JsonResponse({
                'person': [
                    (Person.objects.get(userID=slug)).to_dict()],
                #'URL': URL
            })
        except:
            return JsonResponse({"person":"nothing"})

    if request.method == "DELETE":
        person = get_object_or_404(Person, id=slug)
        person.delete()
        return JsonResponse({})

    return HttpResponseBadRequest("Invalid method")

def persons_api(request):
    '''
        API entry point for list of people
        On POST: Create a new people
    '''
    return JsonResponse({
        'persons': [
            person.to_dict()
            for person in Person.objects.all()
        ]
    })

#@login_required
#def personCreate(request):
#    if request.method == "POST":
#        form = PersonCreationForm(request.POST)
#        form.save()
        

    
