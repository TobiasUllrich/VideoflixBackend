from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from django.contrib import admin
from .models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Individuelle Daten',
            {
                'fields': (
                    'custom',
                    'phone',
                    'address'
                )
            }
        )
    )
