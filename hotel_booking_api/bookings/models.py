from django.db import models

class Booking(models.Model):
    ROOM_TYPES = [
        ('standard', 'Standard'),
        ('deluxe', 'Deluxe'),
        ('suite', 'Suite'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    guest_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    check_in = models.DateField()
    check_out = models.DateField()
    number_of_guests = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.guest_name} - {self.room_type} from {self.check_in} to {self.check_out}"
    
    
    
class Review(models.Model):  # <== Make sure this class is here and not commented out or indented
    guest_name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=20, choices=[
        ('standard', 'Standard'),
        ('deluxe', 'Deluxe'),
        ('suite', 'Suite'),
    ])
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.guest_name} - {self.rating} stars"