# Generated by Django 2.2.16 on 2020-11-07 00:18

import atlantisbot_api.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atlantisbot_api', '0002_auto_20201107_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botmessage',
            name='message_id',
            field=atlantisbot_api.models.DiscordIdField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='discorduser',
            name='discord_id',
            field=atlantisbot_api.models.DiscordIdField(max_length=100),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_id',
            field=atlantisbot_api.models.DiscordIdField(max_length=100),
        ),
        migrations.AlterField(
            model_name='player',
            name='role',
            field=atlantisbot_api.models.DiscordIdField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='playeractivities',
            name='activities_id',
            field=atlantisbot_api.models.DiscordIdField(max_length=100),
        ),
        migrations.AlterField(
            model_name='raidsstate',
            name='time_to_next_message',
            field=atlantisbot_api.models.DiscordIdField(blank=True, max_length=100, null=True, verbose_name='Próxima Mensagem'),
        ),
        migrations.AlterField(
            model_name='team',
            name='author_id',
            field=atlantisbot_api.models.DiscordIdField(max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='invite_channel_id',
            field=atlantisbot_api.models.DiscordIdField(max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='invite_message_id',
            field=atlantisbot_api.models.DiscordIdField(max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='role',
            field=atlantisbot_api.models.DiscordIdField(max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='role_secondary',
            field=atlantisbot_api.models.DiscordIdField(max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_channel_id',
            field=atlantisbot_api.models.DiscordIdField(max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_message_id',
            field=atlantisbot_api.models.DiscordIdField(max_length=100),
        ),
        migrations.AlterField(
            model_name='voiceofseren',
            name='message_id',
            field=atlantisbot_api.models.DiscordIdField(max_length=100),
        ),
        migrations.AlterModelTable(
            name='amigosecretoperson',
            table=None,
        ),
    ]