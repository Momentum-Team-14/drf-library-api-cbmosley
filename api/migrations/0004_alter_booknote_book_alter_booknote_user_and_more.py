# Generated by Django 4.1.1 on 2022-09-15 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_booknote_delete_booknotes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booknote',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='api.book'),
        ),
        migrations.AlterField(
            model_name='booknote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='booktracker',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracking', to='api.book'),
        ),
        migrations.AlterField(
            model_name='booktracker',
            name='status',
            field=models.CharField(choices=[('Reading', 'RG'), ('Read', 'RD'), ('Unread', 'UR')], default='Unread', max_length=100),
        ),
        migrations.AlterField(
            model_name='booktracker',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracking', to=settings.AUTH_USER_MODEL),
        ),
    ]