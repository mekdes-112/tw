from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Meep
# Register your models here.
admin.site.unregister(Group)


#mix profile

class ProfileInline(admin.StackedInline):
    model = Profile

#extend user model

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]

#unregister
admin.site.unregister(User)

#reregistr

admin.site.register(User, UserAdmin)
#admin.site.register(Profile)

admin.site.register(Meep)