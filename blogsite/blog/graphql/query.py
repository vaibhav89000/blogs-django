import graphene

from .types import BlogType, UserType

from .resolvers import AllBlogsResolver, UserBlogsResolver, UserDetailsResolver


class Query(graphene.ObjectType):

    all_blogs = graphene.List(BlogType, resolver=AllBlogsResolver())
    user_blogs = graphene.List(
        BlogType, email=graphene.String(required=True), resolver=UserBlogsResolver()
    )
    user_detail = graphene.Field(
        UserType, email=graphene.String(required=True), resolver=UserDetailsResolver()
    )


# fetch all post (pagination)
# fetch user detail
# fetch user post
# post blog
# like blog
