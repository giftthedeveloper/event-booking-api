import graphene
from graphene_django import DjangoObjectType
from .models import Booking, Event

class BookingType(DjangoObjectType):
    class Meta:
        model = Booking
        fields = ('id', 'name', 'email', 'event', 'booking_date', 'num_ticket', 'is_confirmed', 
                  'dynamic-form-data', 'total_amount')



#create booking
class CreateBooking(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        event = graphene.ID(required=True)
        # booking_date = graphene.DateTime()
        num_ticket = graphene.Int(required=True)
        is_confirmed = graphene.Boolean()
        dynamic_form_data = graphene.JSONString()
    
    booking = graphene.Field(BookingType)

    @classmethod
    def mutate(cls, root, info, name, email, event, num_ticket, is_confirmed, dynamic_form_data=None):
        event_instance = Event.objects.get(pk=event)
        booking = Booking(name=name, email=email,
                          event=event_instance,
                          num_ticket=num_ticket,
                          is_confirmed=is_confirmed,
                          dynamic_form_data=dynamic_form_data)
        booking.save()
        return CreateBooking(booking=booking)
        

#delete booking
class   DeleteBooking(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
       
    
    booking = graphene.Field(BookingType)

    @classmethod
    def mutate(cls, root, info, id):
        booking = Booking.objects.get(id=id)
        booking.delete()
        return f"booking deleted"
        
