# Generated by Django 5.1.6 on 2025-02-11 02:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OriginalURl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Original URL',
                'verbose_name_plural': 'Original URLs',
                'ordering': ['-created_at'],
            },
        ),
        migrations.RemoveIndex(
            model_name='shortenedurl',
            name='shortener_s_origina_f9de52_idx',
        ),
        migrations.AddIndex(
            model_name='originalurl',
            index=models.Index(fields=['url'], name='shortener_o_url_8d8808_idx'),
        ),
        migrations.AlterField(
            model_name='shortenedurl',
            name='original_url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shortened_url', to='shortener.originalurl'),
        ),
        migrations.AddIndex(
            model_name='shortenedurl',
            index=models.Index(fields=['short_code'], name='shortener_s_short_c_f1ca7f_idx'),
        ),
    ]
