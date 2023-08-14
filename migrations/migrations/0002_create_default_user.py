from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_user(apps, schema_editor):
    User = apps.get_model('migrations', 'User')
    if not User.objects.filter(email='test@test.com').exists():
        User.objects.create(
            email='test@test.com',
            password=make_password('1111'),
            login='test',
            username='test',
            is_active=True
        )

def delete_user(apps, schema_editor):
    User = apps.get_model('migrations', 'User')
    try:
        user = User.objects.get(email='test@test.com')
        user.delete()
    except User.DoesNotExist:
        pass


class Migration(migrations.Migration):
    dependencies = [
        ('migrations', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_user, delete_user),
    ]
