# Generated by Django 3.2.13 on 2023-03-11 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='名称/标题')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('orders', models.IntegerField(default=1, verbose_name='排序')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='描述信息')),
            ],
            options={
                'verbose_name': '主机类别',
                'verbose_name_plural': '主机类别',
                'db_table': 'host_category',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='名称/标题')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('orders', models.IntegerField(default=1, verbose_name='排序')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='描述信息')),
                ('ip_addr', models.CharField(blank=True, max_length=500, null=True, verbose_name='连接地址')),
                ('port', models.IntegerField(verbose_name='端口')),
                ('username', models.CharField(max_length=50, verbose_name='登录用户')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='hc', to='host.hostcategory', verbose_name='主机类别')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '主机信息',
                'verbose_name_plural': '主机信息',
                'db_table': 'host',
            },
        ),
    ]
