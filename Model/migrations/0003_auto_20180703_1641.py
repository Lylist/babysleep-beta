# Generated by Django 2.0.6 on 2018-07-03 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0002_auto_20180703_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=11),
        ),
    ]