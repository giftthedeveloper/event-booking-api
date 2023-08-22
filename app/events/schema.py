from graphene_django import DjangoObjectType
from .events_models import Event
import graphene
from account.models import User
from ..event_category.models import EventCategory


class EventType(DjangoObjectType):
    class Meta:
        model = Event
        fields = "__all__"
        # fields = ('organizer', 'name', 'date_time', 'location', 'description', 
        #           'ticket_price', 'tickets_available', 'is_cancelled', 'category', 'qr_code', 'custom_links')
        
class CreateEvent(graphene.Mutation):
    class Arguments:
        organizer = graphene.ID(required=True)
        name = graphene.String(required=True)
        date_time = graphene.DateTime(required=True)
        location = graphene.String(required=True)
        description = graphene.String()
        ticket_price = graphene.Int(required=True)
        tickets_available = graphene.Int(required=True)
        is_cancelled = graphene.Boolean()
        category = graphene.ID(required=True)
        # qr_code = graphene.String()
        custom_link = graphene.String()

    event = graphene.Field(EventType)

    @classmethod
    def mutate (cls, root, info, organizer, name, date_time, location, description ,
                  ticket_price, tickets_available, is_cancelled, category, custom_link):
        organizer_id = User.objects.get(pk=organizer)
        event = Event(organizer=organizer_id,
                      name=name,
                      date_time=date_time,
                      location=location,
                      description=description,
                      ticket_price=ticket_price,
                      tickets_available=tickets_available,
                      is_cancelled=is_cancelled,
                      custom_link=custom_link)
        event.save()
        category_id = EventCategory.objects.get(pk=category)
        event.category.set([category_id])

        return CreateEvent(event=event)
    

