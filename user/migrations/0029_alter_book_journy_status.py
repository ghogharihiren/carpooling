# Generated by Django 3.2.12 on 2022-04-11 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0028_remove_book_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='journy_status',
            field=models.BooleanField(default=False),
        ),
    ]