# Generated by Django 3.2 on 2021-06-04 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0002_auto_20210604_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='goal',
            field=models.FloatField(verbose_name='goal'),
        ),
    ]
