from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0003_auto_20190811_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funds',
            name='amount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='funds',
            name='totalFund',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='funds',
            name='transactionType',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
