from django.contrib import admin
from .  models import *

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class MyUserAdmin(BaseUserAdmin):
    list_display=('username', 'email', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_admin', 'is_active')
    search_fields=('email', 'first_name', 'last_name')
    readonly_fields=('date_joined', 'last_login')
    filter_horizontal=()
    list_filter=('last_login',)
    fieldsets=()

    add_fieldsets=(
        (None,{
            'classes':('wide'),
            'fields':('email', 'username', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )

    ordering=('email',)

# Register your models here.
#for courses
admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Contact)
admin.site.register(Website)
admin.site.register(Commentwebsite)
admin.site.register(Mobile)
admin.site.register(Commentmobile)
admin.site.register(Desktop)
admin.site.register(Commentdesktop)
admin.site.register(Embeded)
admin.site.register(Commentembeded)
admin.site.register(Graphics)
admin.site.register(Commentgraphics)

#for templates
admin.site.register(Websitetemplate)
admin.site.register(Mobiletemplate)
admin.site.register(Desktoptemplate)
admin.site.register(Microsofttemplate)
admin.site.register(Adobetemplate)
