# Generated by Django 2.0.9 on 2018-12-04 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yekpay', '0014_auto_20181120_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='successfull_payment_date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]