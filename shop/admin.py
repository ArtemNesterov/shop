from django.contrib import admin

from .models import Product, ItemType, MyUser, Buy, Return
from .models import Image

admin.site.register(Product)
admin.site.register(Image)
admin.site.register(MyUser)
admin.site.register(ItemType)
admin.site.register(Buy)
admin.site.register(Return)
