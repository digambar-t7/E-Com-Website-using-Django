from django.apps import AppConfig

# django suggested app name
# access it in the settings/installed_apps with entire path 
# i.e. shop.apps.ShopConfig
# or with shortcut 'name'
class ShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'
