# Generated by Django 3.2.13 on 2022-05-18 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_project_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='particularthread',
            name='project_instance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.project'),
        ),
    ]
