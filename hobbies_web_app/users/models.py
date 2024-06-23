from django.db import models
from django.contrib.auth.models import AbstractUser
from pathlib import Path

# Create your models here.
#class User(AbstractUser):
   # hobbies = models.ManyToManyField('Hobbies')

class Person(models.Model):
    userID = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to="profilePicture",blank=True, null=True)
    city = models.CharField(max_length=150)
    email  = models.CharField(max_length=150)
    dob = models.DateField(max_length=150)
    hobbies = models.ManyToManyField(
        'Hobby',
        blank=True,
        symmetrical=False,
        related_name='hobbies'
    )
    #hobbies = models.ForeignKey(Hobby, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.userID
        #return f"{self.name}, {self.image}, {self.email}, {self.city}, {self.dob}"

    def to_dict(self):
        #from django.forms.models import model_to_dict
        #data = self.hobbies.get_queryset()
        #for item in data:
        #    item['product'] = model_to_dict(item['product'])
        return {
            'id': self.id,
            'email': self.email,
            'city': self.city,
            'dob': self.dob,
            'image': self.image.url,
            #'hobbies':item,
            'userID':self.userID
        }

class Hobby(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    #people = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def to_dict(self):
        return({
        "name": self.name,
        "id": self.id,
        "description": self.description
        })

#class Hobbies(models.Model):
#    name = models.CharField(max_length=150)
#    person = models.ForeignKey(
#        Person,
#        on_delete=models.CASCADE,
#        related_name="hobbies",
#    )
#
#    def __str__(self):
#        return f"{self.person}: {self.name}"