# Generated by Django 4.2 on 2023-04-21 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toy_name', models.CharField(max_length=30)),
                ('desc', models.CharField(blank=True, max_length=50)),
                ('price', models.IntegerField(default=20000)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('status', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_email', models.EmailField(max_length=50)),
                ('customer_ph_number', models.CharField(max_length=11)),
                ('customer_address', models.CharField(default='Not specified', max_length=200)),
                ('status', models.CharField(choices=[('0', 'Inactive'), ('1', 'Active')], default=1, max_length=1)),
                ('createdate', models.DateTimeField(auto_now_add=True)),
                ('ordering_toys', models.ManyToManyField(blank=True, to='app1.toy')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]