# Generated by Django 4.2.15 on 2024-08-16 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_like_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
