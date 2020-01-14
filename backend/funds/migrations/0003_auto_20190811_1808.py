from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0002_auto_20190811_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funds',
            name='amount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='funds',
            name='totalFund',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='funds',
            name='transactionType',
            field=models.CharField(default='INITIAL', max_length=20),
        ),
    ]