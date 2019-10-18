from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "core"
    verbose_name = _("Users")

    def ready(self):
        try:
            import {{ cookiecutter.project_slug }}.signals  # noqa F401
        except ImportError:
            pass
