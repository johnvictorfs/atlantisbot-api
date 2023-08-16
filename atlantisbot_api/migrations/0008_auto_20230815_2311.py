# Generated by Django 2.2 on 2023-08-15 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atlantisbot_api', '0007_discorduser_clan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disabledcommand',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='discordingamename',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Nome RuneScape'),
        ),
        migrations.AlterField(
            model_name='discorduser',
            name='clan',
            field=models.CharField(default='Atlantis', max_length=50),
        ),
        migrations.AlterField(
            model_name='discorduser',
            name='discord_name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='discorduser',
            name='ingame_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='doacao',
            name='doador_name',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='doacaogoal',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]