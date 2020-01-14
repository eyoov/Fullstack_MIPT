from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_portfolio_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='cashOnHand',
        ),
    ]
