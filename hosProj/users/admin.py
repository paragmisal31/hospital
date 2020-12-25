from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import User, Patient


class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'fields': (,'username', 'is_patient', 'is_doctor', 'password1', 'password2')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    fieldsets = (
        (None, {
            'fields': ('username', 'is_patient', 'is_doctor', 'password')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    list_display = ['email', 'username', 'is_patient', 'is_doctor']
    search_fields = ('username')
    ordering = ('username',)


admin.site.register(Patient)
admin.site.register(User, UserAdmin)

