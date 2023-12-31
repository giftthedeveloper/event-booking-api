import graphene
from .events.schema import EventType,Event
from .event_category.schema import EventCategoryType, EventCategory, CategoryMutation, EventCategoryMutation, \
    DeleteEventCategoryMutation
from .event_booking.schema import Booking,BookingType, CreateBooking, DeleteBooking
from .events.schema import Event, CreateEvent, UpdateEvent, DeleteEvent


class Query(graphene.ObjectType):
    event_by_id = graphene.Field(EventType, id=graphene.ID(required=True))
    all_events = graphene.List(EventType)
    eventcategory_by_id = graphene.Field(EventCategoryType, id=graphene.ID(required=True))
    all_eventcategory = graphene.List(EventCategoryType)
    booking_by_id = graphene.Field(BookingType, id=graphene.ID(required=True))
    all_bookings = graphene.List(BookingType)

    def resolve_all_events(root, info):
        return Event.objects.all()
    
    def resolve_event_by_id(root, info, id):
        return Event.objects.get(pk=id)
    
    def resolve_all_eventcategory(root, info):
        return EventCategory.objects.all()
    
    def resolve_eventcategory_by_id(root, info, id):
        return EventCategory.objects.get(pk=id)
    
    def resolve_all_bookings(root, info):
        return Booking.objects.all()
    
    def resolve_booking_by_id(root, info, id):
        return Booking.objects.get(pk=id)


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
    delete_events = DeleteEvent.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
