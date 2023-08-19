# Generated by Django 4.2.4 on 2023-08-19 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_time', models.DateTimeField()),
                ('image', models.ImageField(upload_to='events-api/events/')),
                ('location', models.CharField(max_length=2000)),
                ('description', models.TextField()),
                ('ticket_price', models.CharField(max_length=100)),
                ('tickets_available', models.PositiveIntegerField()),
                ('is_cancelled', models.BooleanField(default=False)),
                ('qr_code', models.CharField(max_length=255, unique=True)),
                ('custom_link', models.CharField(help_text='choose a memorable link nameE.g mywedding, giftbirthday', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('rating', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)])),
                ('review_text', models.TextField()),
                ('review_date', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ManyToManyField(related_name='eventscategory', to='app.eventcategory'),
        ),
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('num_ticket', models.PositiveIntegerField(default=1)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('dynamic_form_data', models.JSONField(blank=True, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.event')),
            ],
        ),
    ]