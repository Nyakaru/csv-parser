# Generated by Django 3.0.3 on 2020-02-08 06:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSVParser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.IntegerField(db_index=True)),
                ('contact_name', models.CharField(max_length=20)),
                ('invoice_date', models.DateField(default=django.utils.timezone.now)),
                ('due_date', models.DateField(default=django.utils.timezone.now)),
                ('description', models.CharField(max_length=1000)),
                ('quantity', models.IntegerField(db_index=True)),
                ('unit_amount', models.IntegerField(db_index=True)),
            ],
        ),
    ]
