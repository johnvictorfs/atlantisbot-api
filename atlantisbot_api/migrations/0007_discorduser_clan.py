# Generated by Django 2.2.16 on 2020-11-23 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atlantisbot_api', '0006_auto_20201109_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='discorduser',
            name='clan',
            field=models.CharField(default='Atlantis', max_length=50),
        ),
    ]
