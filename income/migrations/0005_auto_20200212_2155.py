# Generated by Django 3.0.2 on 2020-02-12 16:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('income', '0004_auto_20200212_2150'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='incomecategory',
            unique_together={('user_id', 'title')},
        ),
    ]
