# Generated by Django 3.2.12 on 2022-03-21 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0008_auto_20220311_1420'),
        ('user', '0017_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_id', models.CharField(blank=True, max_length=50, null=True)),
                ('pay_method', models.BooleanField(default=True)),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('feedback', models.TextField(blank=True, null=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.car')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.passenger')),
            ],
        ),
    ]
