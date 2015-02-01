# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stories', '0003_auto_20150131_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='voters',
            field=models.ManyToManyField(related_name='liked_stories', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='story',
            name='moderator',
            field=models.ForeignKey(related_name='moderated_stories', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
