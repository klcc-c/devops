# Generated by Django 3.2.13 on 2023-03-16 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('host', '0003_host_environment'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_beat', models.IntegerField(blank=True, help_text='django-celery-beat调度服务的任务ID，方便我们通过这个id值来控制celery的任务状态', null=True, verbose_name='任务ID')),
                ('task_name', models.CharField(max_length=150, unique=True, verbose_name='任务名称')),
                ('task_cmd', models.TextField(verbose_name='任务指令')),
                ('period_way', models.IntegerField(choices=[(1, '普通计划任务'), (2, '定时一次任务'), (3, '周期计划任务')], default=1, verbose_name='任务周期方式')),
                ('period_content', models.CharField(max_length=32, verbose_name='任务执行周期')),
                ('period_status', models.IntegerField(choices=[(1, '激活'), (2, '停止'), (3, '报错')], default=1)),
            ],
            options={
                'verbose_name': '任务记录表',
                'verbose_name_plural': '任务记录表',
                'db_table': 'schedule_taskschedule',
            },
        ),
        migrations.CreateModel(
            name='TaskHost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hosts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host.host', verbose_name='任务执行主机')),
                ('tasks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.taskschedule', verbose_name='执行的任务')),
            ],
            options={
                'verbose_name': '任务和主机的关系表',
                'verbose_name_plural': '任务和主机的关系表',
                'db_table': 'schedule_taskhost',
            },
        ),
    ]
