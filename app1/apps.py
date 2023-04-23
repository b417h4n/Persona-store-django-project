from django.apps import AppConfig
from django import template
from app1.templatetags.myfilters import intspace

register = template.Library()
register.filter('intspace', intspace)


class App1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app1'
