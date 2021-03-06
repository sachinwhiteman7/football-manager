# Generated by Django 3.0.3 on 2020-02-18 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.PositiveSmallIntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RedCard',
            fields=[
                ('card_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cards.Card')),
                ('reason', models.CharField(choices=[], max_length=256)),
            ],
            bases=('cards.card',),
        ),
        migrations.CreateModel(
            name='YellowCard',
            fields=[
                ('card_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cards.Card')),
                ('reason', models.CharField(choices=[], max_length=256)),
                ('is_second_yellow', models.BooleanField(default=False)),
            ],
            bases=('cards.card',),
        ),
    ]
