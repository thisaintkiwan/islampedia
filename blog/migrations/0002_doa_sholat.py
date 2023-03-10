# Generated by Django 4.1.3 on 2022-12-20 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doa',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('doa', models.CharField(max_length=100)),
                ('ayat', models.CharField(max_length=1000)),
                ('latin', models.TextField()),
                ('artinya', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sholat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField()),
                ('imsyak', models.TimeField()),
                ('shubuh', models.TimeField()),
                ('terbit', models.TimeField()),
                ('dhuha', models.TimeField()),
                ('dhuhur', models.TimeField()),
                ('ashr', models.TimeField()),
                ('magrib', models.TimeField()),
                ('isya', models.TimeField()),
            ],
        ),
    ]
