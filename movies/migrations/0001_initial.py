# Generated by Django 4.2.2 on 2023-06-14 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127)),
                ('duration', models.CharField(blank=True, max_length=10, null=True)),
                ('rating', models.CharField(choices=[('G', 'G'), ('Pg', 'Pg'), ('PG-13', 'Pg 13'), ('R', 'R'), ('NC-17', 'Nc 17')], default='G', max_length=20)),
                ('synopsis', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
