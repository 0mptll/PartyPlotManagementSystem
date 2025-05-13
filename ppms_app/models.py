from django.db import models
from django.contrib.auth.models import User  # Import User model


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_profile')  # Corrected and added related_name
    email = models.EmailField(max_length=50)
    phoneNo = models.CharField(max_length=10)
    password = models.CharField(max_length=128, default='')  # Consider using a proper hashing method
    def __str__(self):
        return f"Customer ID: {self.customer_id}" #Use f-strings


class Admin(models.Model):
    Admin_id = models.AutoField(primary_key=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_profile')  # Corrected and added related_name
    email = models.EmailField(max_length=50)
    phoneNo = models.CharField(max_length=10)
    password = models.CharField(max_length=128, default='')  # Consider using a proper hashing method
    def __str__(self):
        return str(self.name) #changed to string


class Venue(models.Model):
    AVAILABILITY_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    venue_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField()
    amenities = models.TextField()
    pricing = models.CharField(max_length=100)
    availability = models.CharField(max_length=3, choices=AVAILABILITY_CHOICES)
    image = models.ImageField(upload_to='venue_images/', blank=True, null=True)

    def __str__(self):
        return self.venue_name


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    date = models.DateField()
    booking_price = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) # Removed default
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE) # Removed default

    def __str__(self):
        return str(self.date)
    

class Review(models.Model):
    reviewer_name = models.CharField(max_length=100)
    review_text = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.reviewer_name # Added string representation
