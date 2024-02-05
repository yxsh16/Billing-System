from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "billing_sys.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import billing_sys.users.signals  # noqa: F401
        except ImportError:
            pass
