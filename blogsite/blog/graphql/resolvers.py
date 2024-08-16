from graphql import GraphQLError
from ..models import Blog, User
from django.core.exceptions import ObjectDoesNotExist


class AllBlogsResolver:
    """
    This Resolver return all blogs list
    """

    def __call__(self, name, info):
        try:
            return Blog.objects.all()
        except Exception as e:
            raise GraphQLError(str(e))


class UserDetailsResolver:
    """
    This Resolver return all blogs list
    """

    def __call__(self, name, info, **kwargs):
        try:
            if not kwargs.get("email"):
                raise GraphQLError("Email of user is required.")
            email = kwargs.get("email")
            return User.objects.get(email=email)
        except Exception as e:
            raise GraphQLError(str(e))


class UserBlogsResolver:
    """
    This Resolver return user blogs list
    """

    def __call__(self, name, info, **kwargs):
        try:
            print("here i am")
            if not kwargs.get("email"):
                raise GraphQLError("Email of user is required.")
            email = kwargs.get("email")

            user = User.objects.get(email=email)
            user_blogs = Blog.objects.filter(user=user)

            print("user_blogs", user_blogs)
            return user_blogs
        except ObjectDoesNotExist:
            raise GraphQLError("User does not exist")
        except Exception as e:
            raise GraphQLError(str(e))
