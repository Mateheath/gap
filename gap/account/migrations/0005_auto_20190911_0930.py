# Generated by Django 2.2.4 on 2019-09-11 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20190911_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='event',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='event.Event'),
        ),
    ]