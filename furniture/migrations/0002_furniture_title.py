# Generated by Django 3.2.4 on 2021-07-02 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furniture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='furniture',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
