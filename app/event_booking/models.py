from django.db import models
from account.models import User
from events.events_models import Event


class Booking(models.Model):
    """ To handle booking of events from anonymous people"""
    name = models.CharField(max_length=500)
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    num_ticket = models.PositiveIntegerField(default=1)
    is_confirmed = models.BooleanField(default=False)
    dynamic_form_data = models.JSONField(null=True, blank=True)
    
    @property
    def total_amount(self):
        amount = self.event.ticket_price * self.num_tickets
        return amount 
    
    def __str__(self):
        return f"{self.name} - {self.event.name}"
