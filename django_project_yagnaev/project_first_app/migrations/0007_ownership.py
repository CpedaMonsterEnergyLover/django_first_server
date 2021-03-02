# Generated by Django 3.1.7 on 2021-02-21 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0006_license_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateTimeField()),
                ('date_ending', models.DateTimeField()),
                ('car_ownership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.car')),
                ('owner_ownership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.owner')),
            ],
        ),
    ]