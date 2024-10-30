# Generated by Django 5.1.2 on 2024-10-22 02:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_alter_report_options_report_block_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockedReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocked_by', to='reviews.review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocked_reviews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'review')},
            },
        ),
    ]