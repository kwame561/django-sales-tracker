# Generated by Django 2.1.2 on 2019-03-24 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name_of_client', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('category', models.CharField(max_length=100)),
                ('sub_category', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('total_duration', models.DecimalField(decimal_places=2, max_digits=8)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('tools_used', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]