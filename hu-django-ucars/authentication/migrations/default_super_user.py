import os

from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_default_superuser(apps, schema_editor):
    """
    Creates a default super user
    """
    User = apps.get_model('authentication', 'user')
    username = os.environ.get('ADMIN_USERNAME', 'admin')
    password =  os.environ.get('ADMIN_PASS', 'admin@123')
    default_super_user = User(
        username=username,
        is_superuser=True,
        password=make_password(password),
        is_staff=True
    )
    default_super_user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_superuser),
    ]