# Generated by Django 3.1.7 on 2021-04-16 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0003_subscription_credits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='chat_support',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='database_access',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='email_support',
        ),
    ]
