# Generated by Django 5.0.3 on 2024-03-19 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('anonymous', 'Anonymous'), ('published', 'Published')], default='published', max_length=100),
        ),
    ]