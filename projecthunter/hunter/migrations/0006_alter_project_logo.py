# Generated by Django 4.2 on 2023-04-29 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0005_alter_project_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='logo',
            field=models.ImageField(default='image/cv.png', upload_to='image/'),
        ),
    ]
