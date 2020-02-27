from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='year_built',
        ),
    ]
