from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0004_auto_20190811_1813'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='funds',
            options={'verbose_name_plural': 'funds'},
        ),
    ]
