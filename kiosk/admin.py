from django.contrib import admin
from .models import Amenity, RoomRequest

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock')

@admin.register(RoomRequest)
class RoomRequestAdmin(admin.ModelAdmin):
    list_display = ('guest_name', 'room_number', 'amenity', 'timestamp')