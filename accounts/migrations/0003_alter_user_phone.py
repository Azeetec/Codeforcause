# Generated by Django 3.2.13 on 2022-05-17 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_chatmessages_particularthread_project_projectbidders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
