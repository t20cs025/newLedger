from django.contrib import admin
from .models import Ledger, User, RelatedDocument
# Register your models here.

admin.site.register(Ledger)
admin.site.register(User)
admin.site.register(RelatedDocument)