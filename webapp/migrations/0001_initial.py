# Generated by Django 4.2.1 on 2023-06-03 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animes',
            fields=[
                ('id_anime', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_anime', models.CharField(max_length=100)),
            ],
        ),
    ]
