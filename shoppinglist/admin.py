from django.contrib import admin
from .models import Shop, Item
from .models import Ledger, User, RelatedDocument
# Register your models here.

admin.site.register(Shop)
admin.site.register(Item)

admin.site.register(Ledger)
admin.site.register(User)
admin.site.register(RelatedDocument)