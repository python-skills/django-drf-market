from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DirectoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'directory'
    verbose_name = _('Directory')
