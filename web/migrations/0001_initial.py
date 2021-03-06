# Generated by Django 3.0.2 on 2020-02-25 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('token', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('place', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='poster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('field_name', models.ImageField(upload_to='')),
                ('timetolive', models.DateField()),
                ('is_first', models.BooleanField(default=False)),
                ('clients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.client')),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=60)),
                ('text', models.TextField()),
                ('TTL', models.DateField()),
                ('clients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.client')),
            ],
        ),
    ]
