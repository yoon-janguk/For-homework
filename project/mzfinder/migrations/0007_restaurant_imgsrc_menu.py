# Generated by Django 4.0.3 on 2024-05-31 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mzfinder', '0006_review_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='imgSrc',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.TextField()),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mzfinder.restaurant')),
            ],
        ),
    ]