# Generated by Django 3.2.6 on 2022-01-28 23:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_customer', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=15)),
                ('test_provided', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=1000000)),
                ('referral_name', models.CharField(max_length=150)),
                ('discount', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('amount_given', models.DecimalField(decimal_places=2, max_digits=1000000)),
                ('provided_test_results', models.CharField(max_length=250)),
                ('date_of_arrival', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
    ]
