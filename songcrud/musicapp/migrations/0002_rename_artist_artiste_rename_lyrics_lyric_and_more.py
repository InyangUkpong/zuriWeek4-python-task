# Generated by Django 4.1.2 on 2022-10-19 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Artist',
            new_name='Artiste',
        ),
        migrations.RenameModel(
            old_name='Lyrics',
            new_name='Lyric',
        ),
        migrations.RenameField(
            model_name='lyric',
            old_name='sond_id',
            new_name='song_id',
        ),
    ]
