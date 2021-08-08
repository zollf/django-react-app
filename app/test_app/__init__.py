from django.apps import AppConfig

class TestAppConfig(AppConfig):
  name = 'app.test_app'
  label = 'test_app_user'
  verbose_name = 'Test App'

default_app_config = 'app.test_app.TestAppConfig'