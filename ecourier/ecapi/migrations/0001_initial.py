# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('AGENTID', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('group', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=75)),
                ('loc', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AgentCoverage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('agent', models.ForeignKey(to='ecapi.Agent')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourierParcelDesc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sender_name', models.CharField(max_length=255)),
                ('sender_mobile', models.CharField(max_length=255)),
                ('sender_addr', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'courier_parcel_desc',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Coverage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DeliveryTiming',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ecommerce',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('MARCHENTID', models.CharField(max_length=255)),
                ('group', models.CharField(max_length=255)),
                ('siteurl', models.CharField(max_length=255)),
                ('loc', models.IntegerField()),
                ('addr', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=75)),
                ('passwd', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('credits', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('api_secret', models.CharField(max_length=255, null=True, blank=True)),
                ('api_key', models.CharField(max_length=255, null=True, blank=True)),
                ('auth_token', models.CharField(max_length=255, null=True, blank=True)),
                ('is_sms_on', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EcommerceParcelDescription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('REFID', models.CharField(max_length=255)),
                ('coverage', models.IntegerField(null=True, blank=True)),
                ('timing', models.IntegerField(null=True, blank=True)),
                ('weight', models.IntegerField(null=True, blank=True)),
                ('parcel_price', models.IntegerField(null=True, blank=True)),
                ('product_price', models.IntegerField(null=True, blank=True)),
                ('cash_on_delivery', models.BooleanField()),
                ('shipping_agent', models.IntegerField(null=True, blank=True)),
                ('monitoring_agent', models.IntegerField(null=True, blank=True)),
                ('transporter', models.IntegerField(null=True, blank=True)),
                ('is_clear', models.BooleanField()),
                ('comment', models.CharField(max_length=255, null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_at'],
                'db_table': 'EcommerceParcelDescription',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EcommercePriceTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('package_name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('day', models.ForeignKey(to='ecapi.DeliveryTiming')),
                ('place', models.ForeignKey(to='ecapi.Coverage')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Emmiter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gateway',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('api', models.CharField(max_length=255)),
                ('response', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userid', models.CharField(max_length=255)),
                ('act', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
                ('ip', models.CharField(max_length=255)),
                ('useragent', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MailingAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('n_from', models.IntegerField()),
                ('usergroup', models.CharField(max_length=255)),
                ('n_to', models.IntegerField()),
                ('to_usergroup', models.CharField(max_length=255, null=True, blank=True)),
                ('n_message', models.CharField(max_length=255)),
                ('n_time', models.DateTimeField(auto_now_add=True)),
                ('N_REFID', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'notification',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('REFID', models.CharField(max_length=255)),
                ('sendergroup', models.CharField(max_length=255)),
                ('senderid', models.IntegerField(null=True, blank=True)),
                ('r_name', models.CharField(max_length=255)),
                ('r_mobile', models.CharField(max_length=255)),
                ('r_email', models.CharField(max_length=255)),
                ('r_address', models.CharField(max_length=255)),
                ('r_price', models.IntegerField(null=True)),
                ('r_type', models.CharField(max_length=255)),
                ('r_time', models.DateTimeField()),
                ('r_loc_to', models.IntegerField()),
                ('r_loc_from', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
                ('timing', models.IntegerField(null=True)),
                ('courier', models.IntegerField(null=True)),
                ('agent', models.IntegerField(null=True)),
                ('paymentmethod', models.CharField(max_length=255)),
                ('billing', models.IntegerField(null=True)),
                ('paymentclear', models.BooleanField()),
                ('comment', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ParcelDesc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.IntegerField()),
                ('shippingdistance', models.IntegerField()),
                ('deleverytiming', models.IntegerField()),
                ('time', models.CharField(max_length=255)),
                ('comment', models.CharField(max_length=255)),
                ('updatergroup', models.CharField(max_length=255)),
                ('updaterid', models.CharField(max_length=255)),
                ('REFID', models.ForeignKey(to='ecapi.Parcel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ParcelHandOver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ParcelPriceDesc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weightprice', models.IntegerField()),
                ('distanceprice', models.IntegerField()),
                ('timingprice', models.IntegerField()),
                ('totalprice', models.IntegerField()),
                ('listprice', models.CharField(max_length=255)),
                ('currency', models.CharField(max_length=255)),
                ('paymentclear', models.BooleanField()),
                ('paymentcollectorgorup', models.CharField(max_length=255)),
                ('paymentcollectorid', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
                ('REFID', models.ForeignKey(to='ecapi.Parcel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ParcelStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('REFID', models.CharField(max_length=255)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=255)),
                ('updatergroup', models.CharField(max_length=255)),
                ('updaterid', models.CharField(max_length=255)),
                ('loc', models.IntegerField(null=True, blank=True)),
                ('comments', models.CharField(max_length=255)),
                ('view', models.IntegerField()),
            ],
            options={
                'db_table': 'parcelstatus',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ParcelType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('params', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostOffice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('zip', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Thana',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('district', models.ForeignKey(to='ecapi.District')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='timeTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transporter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('group', models.CharField(max_length=255)),
                ('MARCHENT_ID', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('post_code', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'transporter',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transporter_Branch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('passwd', models.CharField(max_length=255)),
                ('loc', models.IntegerField()),
                ('mobile', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('addr', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('mar', models.ForeignKey(to='ecapi.Transporter')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transporter_Branch_Map',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('MAPID', models.CharField(max_length=255)),
                ('loc', models.IntegerField()),
                ('addr', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('relation', models.CharField(max_length=255)),
                ('mar', models.ForeignKey(to='ecapi.Transporter')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transporter_Sub_Branch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('passwd', models.CharField(max_length=255)),
                ('loc', models.IntegerField()),
                ('mobile', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('addr', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('mar', models.ForeignKey(to='ecapi.Transporter_Branch')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Updater',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('REFID', models.CharField(max_length=255)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('updater', models.CharField(max_length=255)),
                ('updaterid', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('loc', models.IntegerField()),
                ('comments', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groups', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserPassword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_group', models.CharField(max_length=255)),
                ('user_id', models.IntegerField(null=True, blank=True)),
                ('user_name', models.CharField(max_length=255, null=True, blank=True)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'password',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=255)),
                ('user_name', models.CharField(max_length=255)),
                ('user_group', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('post_code', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=75)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'general_user',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WeightLimit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='XferAllow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('agents', models.ManyToManyField(related_name='agent_allowed', to='ecapi.Agent')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='XferCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group', models.CharField(max_length=50)),
                ('agentid', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('agent', models.ForeignKey(to='ecapi.Agent')),
                ('transporter', models.ForeignKey(to='ecapi.Transporter')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ZoneMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('totalarea', models.IntegerField(null=True, blank=True)),
                ('post', models.ManyToManyField(to='ecapi.PostOffice')),
            ],
            options={
                'db_table': 'zonemap',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='xferallow',
            name='code',
            field=models.ForeignKey(to='ecapi.XferCode'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='route',
            name='transporter',
            field=models.ForeignKey(to='ecapi.Transporter'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='postoffice',
            name='thana',
            field=models.ForeignKey(to='ecapi.Thana'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='notification',
            name='parcel',
            field=models.ForeignKey(to='ecapi.Parcel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mailingaddress',
            name='postOffice',
            field=models.ForeignKey(to='ecapi.PostOffice'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ecommercepricetable',
            name='weight',
            field=models.ForeignKey(to='ecapi.WeightLimit'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='district',
            name='division',
            field=models.ForeignKey(to='ecapi.Division'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='courierparceldesc',
            name='REFID',
            field=models.ForeignKey(to='ecapi.Parcel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agentcoverage',
            name='zonemap',
            field=models.ForeignKey(to='ecapi.ZoneMap'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agent',
            name='transporter',
            field=models.ForeignKey(to='ecapi.Transporter'),
            preserve_default=True,
        ),
    ]
