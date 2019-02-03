# Generated by Django 2.1 on 2019-02-03 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_auto_20190203_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ankentbl',
            name='FNLCOMMENT',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ankentbl',
            name='FNLFILENM',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='ankentbl',
            name='FNLMONEY',
            field=models.IntegerField(default=3, null=True),
        ),
        migrations.AlterField(
            model_name='ankentbl',
            name='JYUID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ANKENTBL_JYUID', to='hello.USERTBL'),
        ),
        migrations.AlterField(
            model_name='ankentbl',
            name='MDCOMMENT',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ankentbl',
            name='MDMONEY',
            field=models.IntegerField(default=3, null=True),
        ),
        migrations.AlterField(
            model_name='ankentbl',
            name='MIDFILENM',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='ankentbl',
            name='STID',
            field=models.ForeignKey(default='ST0001', on_delete=django.db.models.deletion.CASCADE, to='hello.KOUMOKUM'),
        ),
    ]
