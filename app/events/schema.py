import graphene
from graphene_django import DjangoObjectType
from .events_models import Event
from ..event_category.models import EventCategory
from ..event_category.schema import EventCategoryType
class EventType(DjangoObjectType):
    class Meta:
        model = Event
        fields = "__all__"
        # fields = ('organizer', 'name', 'date_time', 'location', 'description', 
        #           'ticket_price', 'tickets_available', 'is_cancelled', 'category', 'qr_code', 'custom_links')
        
class Query(graphene.ObjectType):
    all_events = graphene.List(EventType)
    all_eventcategory = graphene.List(EventCategoryType)

    def resolve_all_events(root, info):
        return Event.objects.all()
    
    def resolve_all_eventcategory(root, info):
        return EventCategory.objects.all()

schema = graphene.Schema(query=Query)