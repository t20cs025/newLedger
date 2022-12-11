from django import forms
from .models import Item,Ledger

class ItemBuy(forms.Form):
    status = (
        (0,'未購入'),
        (1,'購入')
        )
    item_id = forms.IntegerField(label='ID')
    item_status = forms.ChoiceField(label='STATUS',widget=forms.Select,choices=status)

class ItemIdForm(forms.Form):
    item_id = forms.IntegerField(label='ID')

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'item_url', 'count', 'buy_date', 'shop']

class LedgerForm(forms.ModelForm):
    class Meta:
        model = Ledger
        fields = ['category']