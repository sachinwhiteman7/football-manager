# Generated by Django 3.0.3 on 2020-02-18 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
        ('cards', '0001_initial'),
        ('matches', '0001_initial'),
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matches.Match'),
        ),
        migrations.AddField(
            model_name='card',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.Player'),
        ),
        migrations.AddField(
            model_name='card',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teams.Team'),
        ),
    ]
