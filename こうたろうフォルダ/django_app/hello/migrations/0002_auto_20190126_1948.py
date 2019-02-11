# Generated by Django 2.1 on 2019-01-26 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ANKENTBL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ANKENID', models.CharField(max_length=10)),
                ('ANKENNM', models.CharField(max_length=25)),
                ('CONTENTS', models.CharField(max_length=500)),
                ('REQUESTDATE', models.DateTimeField(auto_now_add=True)),
                ('RECRUITDATE', models.DateTimeField()),
                ('MINPAY', models.IntegerField(default=100)),
                ('MAXPAY', models.IntegerField(default=10000)),
                ('DELIVE', models.DateTimeField()),
                ('MIDFILENM', models.CharField(max_length=30)),
                ('MDCOMMENT', models.CharField(max_length=200)),
                ('MDMONEY', models.IntegerField(default=3)),
                ('FNLFILENM', models.CharField(max_length=30)),
                ('FNLCOMMENT', models.CharField(max_length=200)),
                ('FNLMONEY', models.IntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='HYOKATBL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LINE', models.CharField(max_length=1)),
                ('HYOUKARK', models.CharField(max_length=1)),
                ('HYOUKACMID', models.CharField(max_length=10)),
                ('HYOUKACM', models.CharField(max_length=500)),
                ('ANKENID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.ANKENTBL')),
            ],
        ),
        migrations.CreateModel(
            name='ICHIRANTBL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ANKENID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.ANKENTBL')),
            ],
        ),
        migrations.CreateModel(
            name='KOUMOKUM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ITEMID', models.CharField(max_length=10)),
                ('ITEMNM', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='USERTBL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USERID', models.CharField(max_length=8)),
                ('USERNM', models.CharField(max_length=10)),
                ('PASS', models.CharField(max_length=10)),
                ('NAME', models.CharField(max_length=20)),
                ('BIRTHDAY', models.DateTimeField()),
                ('TEL', models.IntegerField(default=0)),
                ('UNIV', models.CharField(max_length=20)),
                ('FREESPACE', models.CharField(max_length=500)),
                ('MAIL', models.EmailField(max_length=50)),
                ('RANKID', models.CharField(max_length=1)),
                ('ADDRESSID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='KOUMOKUM_ADDRESS', to='hello.KOUMOKUM')),
                ('COUNTRYID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='KOUMOKUM_COUNTRY', to='hello.KOUMOKUM')),
                ('WORKID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='KOUMOKUM_WORK', to='hello.KOUMOKUM')),
            ],
        ),
        migrations.AddField(
            model_name='ichirantbl',
            name='HTUID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ICHIRANTBL_HTUID', to='hello.USERTBL'),
        ),
        migrations.AddField(
            model_name='ichirantbl',
            name='JYUID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ICHIRANTBL_JYUID', to='hello.USERTBL'),
        ),
        migrations.AddField(
            model_name='ichirantbl',
            name='STID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.KOUMOKUM'),
        ),
        migrations.AddField(
            model_name='hyokatbl',
            name='HTUID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='HYOKATBL_HTUID', to='hello.ICHIRANTBL'),
        ),
        migrations.AddField(
            model_name='hyokatbl',
            name='JYUID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='HYOKATBL_JYUID', to='hello.ICHIRANTBL'),
        ),
        migrations.AddField(
            model_name='ankentbl',
            name='HTUID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ANKENTBL_HTUID', to='hello.USERTBL'),
        ),
        migrations.AddField(
            model_name='ankentbl',
            name='JYUID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ANKENTBL_JYUID', to='hello.USERTBL'),
        ),
        migrations.AddField(
            model_name='ankentbl',
            name='STID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.KOUMOKUM'),
        ),
    ]
