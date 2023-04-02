# Generated by Django 4.1.7 on 2023-04-02 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=512, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('fuel', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Petrol'), (1, 'Deisel'), (2, 'Cng')], null=True)),
                ('seat', models.IntegerField(blank=True, null=True)),
                ('enginenumber', models.CharField(blank=True, max_length=100, null=True)),
                ('colour', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.IntegerField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('img_url', models.URLField(blank=True, max_length=512, null=True)),
                ('detail_link', models.URLField(max_length=512)),
            ],
        ),
    ]