from django import forms
from .models import Item,Ledger
from cProfile import label
from unicodedata import category


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

# class DateInput(forms.DateInput):
#     input_type = 'date'
# 
# class TodoForm(forms.ModelForm):
#     class Meta:
#         model = Ledger
#         fields = ['category','input_date','client','consumptionTax','excludingTax','includingTax']
#         wudgets = {'duedate': DateInput(),}