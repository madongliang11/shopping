# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-11-26 16:35
from __future__ import unicode_literals

import apps.main.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': '轮播图', 'verbose_name_plural': '轮播图'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '分类菜单', 'verbose_name_plural': '菜单管理'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': '订单', 'verbose_name_plural': '订单管理'},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name': '商品属性', 'verbose_name_plural': '商品属性'},
        ),
        migrations.AlterModelOptions(
            name='propertyvalue',
            options={'verbose_name': '商品属性值', 'verbose_name_plural': '商品属性值'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': '用户评论', 'verbose_name_plural': '用户评论'},
        ),
        migrations.AlterModelOptions(
            name='shop',
            options={'verbose_name': '商品信息', 'verbose_name_plural': '商品管理'},
        ),
        migrations.AlterModelOptions(
            name='shopcar',
            options={'verbose_name': '购物车', 'verbose_name_plural': '购物车'},
        ),
        migrations.AlterModelOptions(
            name='shopimage',
            options={'verbose_name': '商品图片', 'verbose_name_plural': '商品图片管理'},
        ),
        migrations.AlterModelOptions(
            name='submenu',
            options={'verbose_name': '一级菜单', 'verbose_name_plural': '一级菜单管理'},
        ),
        migrations.AlterModelOptions(
            name='submenu2',
            options={'verbose_name': '二级菜单', 'verbose_name_plural': '二级菜单管理'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '用户管理', 'verbose_name_plural': '用户管理'},
        ),
        migrations.RemoveField(
            model_name='order',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='propertyvalue',
            name='property_id',
        ),
        migrations.RemoveField(
            model_name='propertyvalue',
            name='shop_id',
        ),
        migrations.RemoveField(
            model_name='review',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='shopcar',
            name='oid',
        ),
        migrations.RemoveField(
            model_name='shopcar',
            name='uid',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(db_column='uid', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='main.UserProfile', verbose_name='用户ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='propertyvalue',
            name='property',
            field=models.ForeignKey(db_column='property_id', default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Property', verbose_name='属性ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='propertyvalue',
            name='shop',
            field=models.ForeignKey(db_column='shop_id', default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Shop', verbose_name='商品ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(db_column='uid', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='main.UserProfile', verbose_name='用户ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shopcar',
            name='order',
            field=models.ForeignKey(db_column='oid', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Order', verbose_name='商品ID'),
        ),
        migrations.AddField(
            model_name='shopcar',
            name='user',
            field=models.ForeignKey(db_column='uid', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='main.UserProfile', verbose_name='用户ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=1, verbose_name='添加时间'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='banner',
            name='detail_url',
            field=models.URLField(verbose_name='访问地址'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(storage=apps.main.models.ImageStorage(), upload_to='banner/%Y%m%d', verbose_name='轮播图'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='order',
            field=models.IntegerField(default=1, verbose_name='顺序'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='title',
            field=models.CharField(max_length=100, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cate_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='分类ID'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=255, verbose_name='配送地址'),
        ),
        migrations.AlterField(
            model_name='order',
            name='confirm_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='确认日期'),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_date',
            field=models.DateTimeField(default=1, max_length=0, verbose_name='创建日期'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='交易日期'),
        ),
        migrations.AlterField(
            model_name='order',
            name='mobile',
            field=models.CharField(max_length=11, verbose_name='手机号'),
        ),
        migrations.AlterField(
            model_name='order',
            name='oid',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='订单ID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_code',
            field=models.CharField(max_length=255, verbose_name='订单号'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pay_date',
            field=models.DateTimeField(blank=True, max_length=0, null=True, verbose_name='支付时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='post',
            field=models.CharField(max_length=255, verbose_name='邮编'),
        ),
        migrations.AlterField(
            model_name='order',
            name='receiver',
            field=models.CharField(max_length=255, verbose_name='收货人'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, '正常'), (0, '异常'), (-1, '删除')], default=1, verbose_name='订单状态'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user_message',
            field=models.CharField(max_length=255, verbose_name='附加信息'),
        ),
        migrations.AlterField(
            model_name='property',
            name='cate',
            field=models.ForeignKey(db_column='cate_id', on_delete=django.db.models.deletion.DO_NOTHING, to='main.Category', verbose_name='父菜单'),
        ),
        migrations.AlterField(
            model_name='property',
            name='name',
            field=models.CharField(max_length=64, verbose_name='属性名称'),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='商品属性'),
        ),
        migrations.AlterField(
            model_name='propertyvalue',
            name='pro_value_id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='propertyvalue',
            name='value',
            field=models.CharField(max_length=255, verbose_name='属性值'),
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.CharField(max_length=4000, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='review',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=1, verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='review_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='review',
            name='shop',
            field=models.ForeignKey(db_column='shop_id', on_delete=django.db.models.deletion.DO_NOTHING, to='main.Shop', verbose_name='商品ID'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='cate',
            field=models.ForeignKey(db_column='cate_id', on_delete=django.db.models.deletion.DO_NOTHING, to='main.Category', verbose_name='商品分类'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=1, verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(max_length=100, verbose_name='商品名称'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='original_price',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='原价'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='promote_price',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='折扣价'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shop_id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='商品ID'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='stock',
            field=models.IntegerField(verbose_name='库存'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='sub_title',
            field=models.CharField(max_length=255, verbose_name='商品标题'),
        ),
        migrations.AlterField(
            model_name='shopcar',
            name='car_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='shopcar',
            name='number',
            field=models.IntegerField(default=0, verbose_name='商品数量'),
        ),
        migrations.AlterField(
            model_name='shopcar',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.Shop', verbose_name='商品ID'),
        ),
        migrations.AlterField(
            model_name='shopcar',
            name='status',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='shopimage',
            name='shop',
            field=models.ForeignKey(db_column='shop_id', on_delete=django.db.models.deletion.DO_NOTHING, to='main.Shop', verbose_name='商品ID'),
        ),
        migrations.AlterField(
            model_name='shopimage',
            name='type',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='图片类型'),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='cate',
            field=models.ForeignKey(db_column='cate_id', on_delete=django.db.models.deletion.DO_NOTHING, to='main.Category', verbose_name='父菜单'),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='sub_menu_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='submenu2',
            name='name',
            field=models.CharField(max_length=255, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='submenu2',
            name='sub_menu',
            field=models.ForeignKey(db_column='sub_menu_id', on_delete=django.db.models.deletion.DO_NOTHING, to='main.SubMenu', verbose_name='父菜单'),
        ),
        migrations.AlterField(
            model_name='submenu2',
            name='sub_menu2_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='desc',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='icon',
            field=models.ImageField(default='apps/static/img/default.png', upload_to='upload/img/%Y%m%d', verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(default='110', max_length=11),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='uid',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='用户ID'),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]