from graphene_django import DjangoObjectType
from .events_models import Event

class EventType(DjangoObjectType):
    class Meta:
        model = Event
        fields = "__all__"
        # fields = ('organizer', 'name', 'date_time', 'location', 'description', 
        #           'ticket_price', 'tickets_available', 'is_cancelled', 'category', 'qr_code', 'custom_links')
        
