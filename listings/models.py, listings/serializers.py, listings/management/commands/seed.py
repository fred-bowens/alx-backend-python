cp -r alx_travel_app alx_travel_app_0x00
cd alx_travel_app_0x00

Optionally create a new .env or .sqlite3 file if you want a clean DB.


from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, related_name='bookings', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    guests = models.PositiveIntegerField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.listing.title}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, related_name='reviews', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.listing.title}"

from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
You can extend these with nested serializers or read_only_fields as needed.

from django.core.management.base import BaseCommand
from listings.models import Listing
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed database with sample listings'

    def handle(self, *args, **kwargs):
        fake = Faker()
        Listing.objects.all().delete()
        self.stdout.write('Deleted old listings.')

        for _ in range(10):
            Listing.objects.create(
                title=fake.catch_phrase(),
                description=fake.text(),
                location=fake.city(),
                price_per_night=round(random.uniform(50, 500), 2)
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded 10 listings.'))
⚠


pip install faker

python manage.py makemigrations
python manage.py migrate
python manage.py seed
You should see:

Deleted old listings.
Successfully seeded 10 listings.
