from django.contrib import admin
from .models import Hotel,Location

# Register your models here.

class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'contact', 'email', 'amount')

class LocationAdmin(admin.ModelAdmin):
    fields = ['location_name']

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Location, LocationAdmin)

