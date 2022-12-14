# Generated by Django 2.1.1 on 2022-12-14 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('fileID', models.BigIntegerField(primary_key=True, serialize=False)),
                ('attachedField', models.CharField(max_length=100, verbose_name='属性')),
                ('category', models.BooleanField(choices=[(False, '請求書'), (True, '領収書')], help_text='請求書ならfalse', verbose_name='種別')),
                ('input_date', models.DateField(blank=True, null=True, verbose_name='日付')),
                ('client', models.CharField(max_length=100, verbose_name='相手先')),
                ('consumptionTax_rate', models.PositiveIntegerField(default=10, verbose_name='消費税率')),
                ('consumptionTax', models.PositiveIntegerField(default=0, verbose_name='消費税')),
                ('excludingTax', models.PositiveIntegerField(default=0, verbose_name='税抜金額')),
                ('includingTax', models.PositiveIntegerField(default=0, verbose_name='税込金額')),
                ('registration_date', models.DateField(blank=True, null=True, verbose_name='登録日時')),
                ('approval_date', models.DateField(blank=True, null=True, verbose_name='承認日時')),
                ('image_url', models.URLField(blank=True, null=True, verbose_name='画像url')),
            ],
            options={
                'db_table': '帳簿表',
            },
        ),
        migrations.CreateModel(
            name='RelatedDocument',
            fields=[
                ('relatedFileID', models.BigIntegerField(primary_key=True, serialize=False)),
                ('image_url', models.URLField(blank=True, null=True, verbose_name='画像url')),
            ],
            options={
                'db_table': '関係書類表',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=100)),
                ('userID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'ユーザ表',
            },
        ),
        migrations.AddField(
            model_name='relateddocument',
            name='userID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='D2_app.User', verbose_name='user'),
        ),
        migrations.AddField(
            model_name='ledger',
            name='userID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='D2_app.User', verbose_name='user'),
        ),
    ]
