# Generated by Django 3.2.5 on 2021-10-23 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20211023_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreplacements',
            name='category',
            field=models.CharField(choices=[('Addition', 'Addition'), ('Deduction', 'Deduction')], max_length=12, verbose_name='Category'),
        ),
        migrations.DeleteModel(
            name='UserDiscounts',
        ),
    ]
