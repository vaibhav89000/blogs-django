from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40, unique=True)
    gender = models.CharField(
        max_length=6,
        choices=(
            ("MALE", "Male"),
            ("FEMALE", "Female"),
        ),
    )
    address1 = models.CharField(max_length=20)
    address2 = models.CharField(max_length=20, blank=True, null=True)
    district = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    pin_code = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    # Method to get the like count for this blog
    def like_count(self):
        return self.likes.count()

    # Method to get the users who liked this blog
    def liked_users(self):
        return [like.user for like in self.likes.all()]


class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked")

    class Meta:
        unique_together = ("blog", "user")

    def __str__(self):
        return f"{self.user.name} liked {self.blog.title}"
