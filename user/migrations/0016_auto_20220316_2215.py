# Generated by Django 3.2.12 on 2022-03-16 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_book_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='car',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='uid',
        ),
        migrations.DeleteModel(
            name='book',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
