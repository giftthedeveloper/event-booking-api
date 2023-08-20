import graphene
from graphene_django import DjangoObjectType
from .models import EventCategory

class EventCategoryType(DjangoObjectType):
    class Meta:
        model = EventCategory
        fields = "__all__"

class Query(graphene.ObjectType):
    all_eventcategory = graphene.List(EventCategoryType)

    def resolve_all_eventcategory(root, info):
        return EventCategory.objects.all()
    

schema = graphene.Schema(query=Query)