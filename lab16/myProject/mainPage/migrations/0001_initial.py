# Generated by Django 3.2.9 on 2021-12-12 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Производитель')),
                ('country', models.CharField(max_length=128, verbose_name='Страна')),
                ('CEO', models.CharField(max_length=128, verbose_name='Ген. директор')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('address', models.CharField(max_length=128, verbose_name='Адрес')),
                ('status', models.CharField(max_length=128, verbose_name='Статус')),
            ],
        ),
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=128, verbose_name='Модель')),
                ('price', models.IntegerField(max_length=10, verbose_name='Цена')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainPage.shop')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainPage.manufacturer')),
            ],
        ),
    ]
