# Generated by Django 4.2 on 2023-04-29 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enter', '0003_alter_profile_options_alter_user_reputation_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='static/image/profile.png', upload_to='static/images'),
        ),
    ]
