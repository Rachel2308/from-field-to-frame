# Generated by Django 3.2.4 on 2021-07-22 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20210722_2301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='original_bag',
            new_name='original_basket',
        ),
    ]