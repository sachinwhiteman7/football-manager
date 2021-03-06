# Generated by Django 3.0.3 on 2020-02-20 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=256)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='team/logos')),
                ('address_line_1', models.CharField(default='', max_length=256)),
                ('address_line_2', models.CharField(default='', max_length=256)),
                ('city', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='VenuePhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='photos/venue')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venues.Venue')),
            ],
        ),
    ]
