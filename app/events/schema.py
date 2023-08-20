import graphene
from graphene_django import DjangoObjectType
from .events_models import Event

class EventType(DjangoObjectType):
    class Meta:
        model = Event
        fields = "__all__"
        # fields = ('organizer', 'name', 'date_time', 'location', 'description', 
        #           'ticket_price', 'tickets_available', 'is_cancelled', 'category', 'qr_code', 'custom_links')
        
class Query(graphene.ObjectType):
    all_events = graphene.List(EventType)
    
    def resolve_all_events(root, info):
        return Event.objects.all()

schema = graphene.Schema(query=Query)