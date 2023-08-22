import graphene
from .events.schema import EventType,Event
from .event_category.schema import EventCategoryType, EventCategory, CategoryMutation, EventCategoryMutation, \
    DeleteEventCategoryMutation
from .event_booking.schema import Booking,BookingType, CreateBooking, DeleteBooking
from .events.schema import Event, CreateEvent, UpdateEvent


class Query(graphene.ObjectType):
    all_events = graphene.List(EventType)
    all_eventcategory = graphene.List(EventCategoryType)
    all_bookings = graphene.List(BookingType)

    def resolve_all_events(root, info):
        return Event.objects.all()
    
    def resolve_all_eventcategory(root, info):
        return EventCategory.objects.all()
    
    def resolve_all_bookings(root, info):
        return Booking.objects.all()


#for create, update and delete methods  
class Mutation(graphene.ObjectType):
    #category
    add_category = CategoryMutation.Field()
    update_category = EventCategoryMutation.Field()
    delete_category = DeleteEventCategoryMutation.Field()
    
    #bookings
    add_booking = CreateBooking.Field()
    delete_booking = DeleteBooking.Field()

    #events
    add_events = CreateEvent.Field()
    update_events = UpdateEvent.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
