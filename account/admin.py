from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm , CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form =CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','first_name','email' , 'is_staff',  ]
    
    
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ('age','about', 'photo')}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ('age','about', 'photo' )}),)


admin.site.register(CustomUser, CustomUserAdmin)
