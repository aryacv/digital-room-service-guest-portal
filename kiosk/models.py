from django.db import models

class Amenity(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=200, blank=True)

    # This tells Django Admin to show the actual name of the amenity
    def __str__(self):
        return self.name

class RoomRequest(models.Model):
    guest_name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10)
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    # This fixes the "empty/generic object" view in the admin panel!
    def __str__(self):
        return f"Room {self.room_number} - {self.guest_name} ({self.amenity.name})"