from django.contrib import admin

from hobbies.models import Hobby

class HobbyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Hobby, HobbyAdmin)
