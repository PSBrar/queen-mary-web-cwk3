from django.db import models

# Create your models here.
class Hobby(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def to_dict(self):
        return({
        "name": self.name,
        "id": self.id,
        "description": self.description
        })
