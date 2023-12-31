# Generated by Django 4.2.6 on 2023-10-19 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='core.country'),
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='core.brand'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.car'),
        ),
    ]
