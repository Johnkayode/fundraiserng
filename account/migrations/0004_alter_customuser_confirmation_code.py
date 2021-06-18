# Generated by Django 3.2.4 on 2021-06-10 18:39

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_customuser_confirmation_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='confirmation_code',
            field=models.IntegerField(default=account.models.gen_confirmation_code, null=True, verbose_name='confirmation code'),
        ),
    ]
