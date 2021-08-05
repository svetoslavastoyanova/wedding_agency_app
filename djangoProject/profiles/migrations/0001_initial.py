# Generated by Django 3.2.5 on 2021-07-27 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wedding_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('first_name', models.CharField(blank=True, max_length=20)),
                ('last_name', models.CharField(blank=True, max_length=20)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('profile_image', models.ImageField(blank=True, upload_to='profiles')),
                ('is_complete', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='wedding_auth.weddinguser')),
            ],
        ),
    ]
