# Generated by Django 2.0.4 on 2018-09-29 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='marks',
            field=models.IntegerField(null=True),
        ),
    ]
