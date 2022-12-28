# Generated by Django 4.1.1 on 2022-12-23 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='world',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CONTINENT', models.CharField(max_length=100)),
                ('COUNTRY', models.CharField(max_length=100)),
                ('p1', models.CharField(max_length=50, null=True)),
                ('p2', models.CharField(max_length=50, null=True)),
                ('p3', models.CharField(max_length=50, null=True)),
                ('p4', models.CharField(max_length=50, null=True)),
                ('p5', models.CharField(max_length=50, null=True)),
                ('p6', models.CharField(max_length=50, null=True)),
                ('p7', models.CharField(max_length=50, null=True)),
                ('p8', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Park',
        ),
    ]