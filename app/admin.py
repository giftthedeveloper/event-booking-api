from django.contrib import admin
from .models import Event, EventCategory, Booking

admin.site.register(Event)
admin.site.register(EventCategory)
admin.site.register(Booking)