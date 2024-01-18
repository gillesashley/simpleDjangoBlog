from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'name', 'is_staff']
    list_display_links = ['email', 'username']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'groups']
    search_fields = ['first_name', 'last_name', 'username', 'email']
    ordering = ['first_name', 'last_name']
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ('name', 'age')}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ('name', 'email', 'age')}),)


admin.site.register(CustomUser, CustomUserAdmin)
