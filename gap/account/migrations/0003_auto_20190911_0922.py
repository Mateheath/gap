# Generated by Django 2.2.4 on 2019-09-11 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_remove_event_participant'),
        ('account', '0002_user_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='event',
        ),
        migrations.AddField(
            model_name='user',
            name='event',
            field=models.ManyToManyField(to='event.Event'),
        ),
    ]