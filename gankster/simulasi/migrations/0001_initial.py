# Generated by Django 4.2.1 on 2023-06-12 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Simulasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('panjang', models.CharField(max_length=15)),
                ('lebar', models.CharField(max_length=15)),
            ],
        ),
    ]
