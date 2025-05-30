# Generated by Django 3.1.2 on 2020-10-23 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0059_auto_20201023_0442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalhodan',
            name='status',
            field=models.IntegerField(choices=[(0, 'Chưa xác minh'), (1, 'Cần ứng cứu gấp'), (2, 'Không gọi được'), (3, 'Đã được cứu'), (4, 'Gặp nạn'), (5, 'Đã gửi hỗ trợ'), (5, 'Cần thức ăn'), (6, 'Cần thuốc men'), (7, 'Đã ổn')], default=0, verbose_name='Tình trạng'),
        ),
        migrations.AlterField(
            model_name='hodan',
            name='status',
            field=models.IntegerField(choices=[(0, 'Chưa xác minh'), (1, 'Cần ứng cứu gấp'), (2, 'Không gọi được'), (3, 'Đã được cứu'), (4, 'Gặp nạn'), (5, 'Đã gửi hỗ trợ'), (5, 'Cần thức ăn'), (6, 'Cần thuốc men'), (7, 'Đã ổn')], default=0, verbose_name='Tình trạng'),
        ),
    ]
