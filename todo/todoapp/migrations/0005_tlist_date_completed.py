# Generated by Django 4.2.6 on 2023-11-03 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_alter_tlist_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='tlist',
            name='date_completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
