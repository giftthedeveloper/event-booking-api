import graphene
from .events.schema import EventType,Event
from .event_category.schema import EventCategoryType, EventCategory


class Query(graphene.ObjectType):
    all_events = graphene.List(EventType)
    all_eventcategory = graphene.List(EventCategoryType)

    def resolve_all_events(root, info):
        return Event.objects.all()
    
    def resolve_all_eventcategory(root, info):
        return EventCategory.objects.all()

schema = graphene.Schema(query=Query)