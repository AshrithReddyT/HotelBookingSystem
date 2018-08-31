from django.contrib import admin
from .models import User, Manager

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')

class ManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'hotel')

admin.site.register(User, UserAdmin)
admin.site.register(Manager, ManagerAdmin)
