# Generated by Django 3.2.12 on 2023-03-04 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_1', models.CharField(max_length=100)),
                ('team_2', models.CharField(max_length=100)),
                ('team_1_score', models.IntegerField()),
                ('team_2_score', models.IntegerField()),
            ],
        ),
    ]
