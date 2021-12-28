# Generated by Django 3.2.5 on 2021-10-23 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20211020_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdiscounts',
            name='category',
            field=models.CharField(choices=[('REPLACEMENT', 'REPLACEMENT'), ('DISCOUNTS', 'DISCOUNTS')], max_length=12, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='userreplacements',
            name='category',
            field=models.CharField(choices=[('REPLACEMENT', 'REPLACEMENT'), ('DISCOUNTS', 'DISCOUNTS')], max_length=12, verbose_name='Category'),
        ),
    ]
