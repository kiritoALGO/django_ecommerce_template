from django.apps import AppConfig
# from django.db.utils import OperationalError

class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shippingRate'

    # def ready(self):
    #     from shippingRate.models import ShippingRate
    #     default_rates = [
    #         ("6th of October", 50),
    #         ("Al Sharqia", 80),
    #         ("Alexandria", 80),
    #         ("Aswan", 80),
    #         ("Asyut", 80),
    #         ("Beheira", 80),
    #         ("Beni Suef", 80),
    #         ("Cairo", 50),
    #         ("Dakahlia", 80),
    #         ("Damietta", 80),
    #         ("Faiyum", 80),
    #         ("Gharbia", 80),
    #         ("Giza", 50),
    #         ("Helwan", 80),
    #         ("Ismailia", 80),
    #         ("Kafr el-Sheikh", 80),
    #         ("Luxor", 80),
    #         ("Matrouh", 80),
    #         ("Minya", 80),
    #         ("Monufia", 80),
    #         ("New Valley", 80),
    #         ("North Sinai", 80),
    #         ("Port Said", 80),
    #         ("Qalyubia", 80),
    #         ("Red Sea", 80),
    #         ("Sohag", 80),
    #         ("South Sinai", 80),
    #         ("Suez", 80),
    #     ]
        
    #     try:
    #         if not ShippingRate.objects.exists():
    #             for governorate, price in default_rates:
    #                 ShippingRate.objects.create(governorate=governorate, shipping_price=price)
    #     except OperationalError:
    #         # This handles the case where migrations haven't been run yet
    #         pass
