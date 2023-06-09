# Generated by Django 4.2 on 2023-04-29 06:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('logo', models.ImageField(upload_to='static/images')),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('git', models.URLField(blank=True, max_length=254)),
                ('uurl', models.UUIDField(default=uuid.uuid4, help_text='Unique identifier for the referral invitation to the team', verbose_name='Invite ref')),
            ],
            options={
                'verbose_name': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('grade', models.CharField(choices=[('j', 'Junior'), ('m', 'Middle'), ('s', 'Senior'), ('l', 'Team lead')], default='j', max_length=1, verbose_name='Grade')),
            ],
            options={
                'verbose_name': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Skills',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enter.profile')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hunter.project')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hunter.role')),
            ],
            options={
                'verbose_name': 'Teams',
            },
        ),
        migrations.CreateModel(
            name='Project_Reputation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hunter.project')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enter.profile')),
            ],
            options={
                'verbose_name': 'Project_Reputations',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='skills',
            field=models.ManyToManyField(blank=True, to='hunter.skill'),
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, to='hunter.tag'),
        ),
    ]
