# Generated by Django 3.0.3 on 2020-02-19 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0001_initial'),
        ('players', '0001_initial'),
        ('cards', '0002_auto_20200218_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='match',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='matches.Match'),
        ),
        migrations.AlterField(
            model_name='card',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='players.Player'),
        ),
    ]
