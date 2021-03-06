# Generated by Django 3.0.3 on 2020-02-20 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
        ('goals', '0002_auto_20200218_1105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='is_own_goal',
        ),
        migrations.AddField(
            model_name='goal',
            name='goal_type',
            field=models.CharField(default='goal', max_length=32),
        ),
        migrations.AlterField(
            model_name='goal',
            name='assisted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assist', to='players.Player'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='scored_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='scorer', to='players.Player'),
        ),
    ]
