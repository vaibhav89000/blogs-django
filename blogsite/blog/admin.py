from django.contrib import admin

from .models import Blog, Like, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "address1",
        "address2",
        "gender",
        "district",
        "state",
        "pin_code",
    )


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "title",
        "description",
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "blog",
        "user",
    )
