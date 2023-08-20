import graphene
from graphene_django import DjangoObjectType
from .models import Booking

class BookingType(DjangoObjectType):
    class Meta:
        model = Booking
        fields = "__all__"


