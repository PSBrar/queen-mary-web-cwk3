from django.http.response import HttpResponse
from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, PersonCreationForm
import os
from users.models import Person, Hobby
from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    
  
    return render(request, 'users/register.html', {'form': form})


#@login_required 
def profile(request):
    current_user = request.user
    #print (current_user)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, request.FILES)
        #print("maybe")
        if form.is_valid():
            form.instance.userID = str(current_user)
            form.save()
            #print("yes")
    else:    
        form=PersonCreationForm()
        #print("no")
        #print(request)
    
    return render(request, 'users/profile.html', {'form':form})

def edit(request):
    current_user = request.user
    print(current_user)
    current_profile = Person.objects.get(userID=current_user)
    #print (current_user)
    form = PersonCreationForm(request.POST,instance=current_profile)
        #print("maybe")
    #if form.is_valid():
    form.instance.userID = str(current_user)
    form.save()
    return redirect("/")
        #print("yes")
    #else:    
        #form=PersonCreationForm()
        #print("no")
        #print(request)
    
    return render(request, 'users/profile.html', {'form':form})

def sendURL(request, slug):
    persons = (Person.objects.get(userID=slug))
    #persons.image = "media/"+str(persons.image)
    allPersons = (Person.objects.all())
    numberList = []
    #print(allPersons)
    # use data

    #for i in enumerate(allPersons):
    #    print (i.hobbies.values)

    #for person in allPersons:
    #    print(person)
    #    for i in person.hobbies.values:
    #        if (i == persons.hobbies.values):
    #            print(1)
    #for i in persons.hobbies.values.name:
    #    for x in allPersons.hobbies.values.names
    return render(request, 'users/profilePage.html', {
        "personObject": persons,
        "allPersonsObject": allPersons
    })


#def persons_view(request):
#    persons = Person.objects.all()
#    request.session['last_visit'] = str(timezone.now())
#    return render(request, 'users/profile.html', {
#        'persons': persons,
#        'user': request.user,
#    })


#def person_view(request):
#    try:
#        person = Person.objects.all()
#        return render(request, 'users/profile.html', {
#            'person': person,
#        })
#    except Person.DoesNotExist:
#        return HttpResponse(f"This is invalid")
    