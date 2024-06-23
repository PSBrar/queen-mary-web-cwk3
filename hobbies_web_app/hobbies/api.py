from django.http import JsonResponse
from users.models import Hobby
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json

def hobbies_api(request):
    '''
    entry point for doing GET request for hobbies list
    '''
    return JsonResponse({
        'hobbies': [
            Hobby.to_dict()
            for Hobby in Hobby.objects.all()
        ]
    })


@csrf_exempt
def create_hobbies_api(request):
    '''
    entry point for doing GET request for hobbies list
    '''
    if request.method == "POST":
        body = json.loads(request.body.decode("utf-8"))
        hname = body["hname"]
        hdescription = body["hdescription"]
        hobby1 = Hobby(name=hname, description=hdescription)
        hobby1.save()
        return JsonResponse({})
