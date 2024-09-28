# Generated by Django 5.1.1 on 2024-09-28 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date_time', models.DateTimeField()),
                ('venue', models.CharField(max_length=255)),
                ('ticket_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_tickets', models.IntegerField()),
                ('remaining_tickets', models.IntegerField()),
            ],
        ),
    ]
