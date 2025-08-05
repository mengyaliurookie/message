from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.template.defaultfilters import date
from django.utils import timezone

# 将Jinja2模板定义到Django环境中
def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    env.filters.update({
        'localtime':lambda value:timezone.localtime(value) if value else None,
        'date':date,
        'naturaltime':naturaltime,
    })
    return env