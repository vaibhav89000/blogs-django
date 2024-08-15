from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
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
    user = models.ForeignKey(User, models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Like(models.Model):
    post = models.ForeignKey(Blog, models.CASCADE)
    count = models.IntegerField(default=0)
    users = models.ManyToManyField(User, models.CASCADE)

    def increase_count(self):
        self.count += 1

    def decrease_count(self):
        self.count -= 1
