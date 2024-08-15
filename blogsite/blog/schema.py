import graphene
from blog.graphql.query import Query
from blog.graphql.mutations import Mutation


# schema = graphene.Schema(query=Query, mutation=Mutation)
schema = graphene.Schema(query=Query, mutation=Mutation)
