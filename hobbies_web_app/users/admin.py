from django.contrib import admin

from users.models import Person, Hobby

class PersonAdmin(admin.ModelAdmin):
    pass

#@admin.register(Person)
#class PersonAdmin(admin.ModelAdmin):
#    list_display = ['name', 'image', 'dob', 'city', 'email']

class HobbyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Person, PersonAdmin)
admin.site.register(Hobby, HobbyAdmin)

#@admin.register(Hobby)
#class HobbiesAdmin(admin.ModelAdmin):
#    list_display = ['person', 'name']
#    list_filter = ['person']