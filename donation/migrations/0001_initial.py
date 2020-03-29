# Generated by Django 3.0.4 on 2020-03-19 14:32

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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=264)),
                ('type', models.CharField(choices=[('FUNDACJA', 'Fundacja'), ('ORGANIZACJA POZARZĄDOWA', 'Organizacja pozarządowa'), ('ZBIÓRKA LOKALNA', 'Zbiórka lokalna')], default='FUNDACJA', max_length=64)),
                ('category', models.ManyToManyField(to='donation.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=64)),
                ('phone_number', models.IntegerField(default=None)),
                ('city', models.CharField(max_length=32)),
                ('zip_code', models.CharField(max_length=12)),
                ('pick_up_date', models.CharField(max_length=32)),
                ('pick_up_time', models.CharField(max_length=32)),
                ('pick_up_comment', models.CharField(max_length=128)),
                ('categories', models.ManyToManyField(to='donation.Category')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donation.Institution')),
                ('user', models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
