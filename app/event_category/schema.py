import graphene
from graphene_django import DjangoObjectType
from .models import EventCategory

class EventCategoryType(DjangoObjectType):
    class Meta:
        model = EventCategory
        fields = "__all__"

