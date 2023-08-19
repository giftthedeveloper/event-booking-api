from django.db import models
from account.models import User
from ..event_category.models import EventCategory

class Event(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    image= models.ImageField(upload_to='events-api/events/') 
    location = models.CharField(max_length=2000)
    description = models.TextField()
    ticket_price = models.CharField(max_length=100)
    tickets_available = models.PositiveIntegerField()
    is_cancelled = models.BooleanField(default=False)
    category = models.ManyToManyField(EventCategory, related_name='eventscategory')
    qr_code = models.CharField(max_length=255, unique=True)
    custom_link = models.CharField(max_length=255, help_text='choose a memorable link nameE.g mywedding, giftbirthday')


    def __str__(self):
        return self.name
