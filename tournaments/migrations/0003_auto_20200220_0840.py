# Generated by Django 3.0.3 on 2020-02-20 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0001_initial'),
        ('teams', '0001_initial'),
        ('tournaments', '0002_auto_20200219_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='name',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='stage',
            name='name',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='no_of_teams',
            field=models.PositiveSmallIntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='venue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='venues.Venue'),
        ),
        migrations.AlterUniqueTogether(
            name='teampointstable',
            unique_together={('points_table', 'team')},
        ),
        migrations.CreateModel(
            name='TournamentPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=1024)),
                ('photo', models.ImageField(upload_to='photos/tournaments')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Tournament')),
            ],
        ),
    ]
