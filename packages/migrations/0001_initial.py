# Generated by Django 2.1.10 on 2020-07-05 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('itineraries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('itineraries', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='itineraries.Itinerary')),
            ],
        ),
    ]
