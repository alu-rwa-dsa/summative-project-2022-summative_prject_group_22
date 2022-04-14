# Generated by Django 4.0.4 on 2022-04-14 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=255)),
                ('arrived_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-arrived_at'],
            },
        ),
        migrations.CreateModel(
            name='Teller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('wait_time', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Customers',
        ),
        migrations.AddField(
            model_name='customer',
            name='teller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.teller'),
        ),
    ]