# Generated by Django 2.2.16 on 2020-11-07 00:11

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('atlantisbot_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvLogState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlayerActivities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activities_id', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('team_id', models.CharField(max_length=10, unique=True)),
                ('title', models.CharField(max_length=30)),
                ('size', models.IntegerField()),
                ('role', models.CharField(max_length=100)),
                ('role_secondary', models.CharField(max_length=100)),
                ('author_id', models.CharField(max_length=100)),
                ('invite_channel_id', models.CharField(max_length=100)),
                ('invite_message_id', models.CharField(max_length=100)),
                ('team_channel_id', models.CharField(max_length=100)),
                ('team_message_id', models.CharField(max_length=100)),
                ('secondary_limit', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VoiceOfSeren',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_voice_one', models.CharField(max_length=10)),
                ('current_voice_two', models.CharField(max_length=10)),
                ('message_id', models.CharField(max_length=100)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelManagers(
            name='discorduser',
            managers=[
                ('discord', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RenameField(
            model_name='doacao',
            old_name='ammount',
            new_name='amount',
        ),
        migrations.AlterField(
            model_name='amigosecretostate',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='amigosecretostate',
            name='premio_maximo',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='amigosecretostate',
            name='premio_minimo',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='amigosecretostate',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='raidsstate',
            name='time_to_next_message',
            field=models.CharField(max_length=100, blank=True, null=True, verbose_name='Próxima Mensagem'),
        ),
        migrations.AlterModelTable(
            name='amigosecretostate',
            table=None,
        ),
        migrations.AlterModelTable(
            name='disabledcommand',
            table=None,
        ),
        migrations.AlterModelTable(
            name='raidsstate',
            table=None,
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_id', models.CharField(max_length=100)),
                ('role', models.CharField(blank=True, max_length=100, null=True)),
                ('in_team', models.BooleanField(default=False)),
                ('substitute', models.BooleanField(default=False)),
                ('secondary', models.BooleanField(default=False)),
                ('team', models.ForeignKey(db_column='team', on_delete=django.db.models.deletion.CASCADE, related_name='players', to='atlantisbot_api.Team', verbose_name='Time')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BotMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.CharField(max_length=100, unique=True)),
                ('team', models.ForeignKey(db_column='team', on_delete=django.db.models.deletion.CASCADE, related_name='bot_messages', to='atlantisbot_api.Team', verbose_name='Time')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
