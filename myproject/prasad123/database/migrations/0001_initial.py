# Generated by Django 2.2.2 on 2019-07-01 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_name', models.CharField(max_length=264)),
                ('e_id', models.IntegerField(unique=True)),
                ('dept', models.CharField(max_length=264)),
            ],
        ),
    ]
