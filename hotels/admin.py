from django.contrib import admin
from .models import Hotel,Room

# Register your models here.

class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'contact', 'email', 'rating')

class RoomAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'type_name','occupancy','room_type','maximum','available','cost')

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Room, RoomAdmin)
