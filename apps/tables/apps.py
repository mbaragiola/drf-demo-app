from django.apps import AppConfig


class TablesConfig(AppConfig):
    name = "apps.tables"
    verbose = "Tables"

    def ready(self):
        pass
