from django.contrib import admin
from .models import Admin, Customer, Venue, Booking, Review

# Register Customer model
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'name', 'email', 'phoneNo', 'password')

# Register Booking model
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'date', 'booking_price', 'customer_id', 'get_venue_name')

    def get_venue_name(self, obj):
        return obj.venue.venue_name

    get_venue_name.short_description = 'Venue Name'

# Register Venue model
@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('venue_name', 'location', 'capacity', 'amenities', 'pricing', 'availability')

# Register Admin model
@admin.register(Admin)
class AdminuserAdmin(admin.ModelAdmin):
    list_display = ('Admin_id', 'name', 'email', 'phoneNo', 'password')

    def Admin_id(self, obj):
        return obj.Admin_id

# Register Review model
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer_name', 'review_text', 'created_at')
