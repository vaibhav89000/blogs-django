# Generated by Django 4.2.15 on 2024-08-15 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('blog', 'user')},
        ),
    ]
