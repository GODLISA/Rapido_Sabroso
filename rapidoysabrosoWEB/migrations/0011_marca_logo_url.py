# Generated by Django 5.1.2 on 2024-10-16 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapidoysabrosoWEB', '0010_pageselector_logo_selector'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca',
            name='logo_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
