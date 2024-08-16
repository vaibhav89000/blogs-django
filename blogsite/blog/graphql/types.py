import graphene
from graphene_django import DjangoObjectType

from ..models import Blog, User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class BlogType(DjangoObjectType):
    class Meta:
        model = Blog

    user = graphene.Field(UserType)

    def resolve_user(self, info):
        return self.user
