import graphene
from graphene_django import DjangoObjectType
from .models import EventCategory

class EventCategoryType(DjangoObjectType):
    class Meta:
        model = EventCategory
        fields = "__all__"

#for creating
class CategoryMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()

    category = graphene.Field(EventCategoryType)

    @classmethod
    def mutate(cls, root, info, name, description):
        category = EventCategory(name=name, description=description)
        category.save()
        return CategoryMutation(category=category)
    

 #for updating data   
class EventCategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)
        description = graphene.String()

    category = graphene.Field(EventCategoryType)

    @classmethod
    def mutate(cls, root, info, id, name, description):
        category = EventCategory.objects.get(id=id)
        category.name = name
        category.description = description
        category.save()
        return EventCategoryMutation(category=category)
    
 #for deleting data   
class DeleteEventCategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    category = graphene.Field(EventCategoryType)

    @classmethod
    def mutate(cls, root, info, id):
        category = EventCategory.objects.get(id=id)
        category.delete()
        return f"category deleted"
    
    