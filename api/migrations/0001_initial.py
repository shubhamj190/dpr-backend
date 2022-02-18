from django.db import migrations
from django.db.migrations import operations
from api.user.models import Customuser

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user=Customuser(name='shubham',email="shubhamjadhav190@gmail.com",is_staff=True, is_superuser=True, phone='8007454373')

        user.set_password('12345')
        user.save()

    dependencies = [
        ]

    operations=[
            migrations.RunPython(seed_data),
        ]