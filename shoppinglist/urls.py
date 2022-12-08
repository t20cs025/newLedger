from django.urls import path
from .views import ItemList, ItemEditView,ItemShowView,ItemDeleteView,ItemAddView


app_name = 'shoppinglist'
urlpatterns = [
    path('list/',ItemList.as_view(),name='list'),
    path('add', ItemAddView.as_view(), name='add'),
    
    path('edit/<int:pk>', ItemEditView.as_view(),name='edit'),

    path('show', ItemShowView.as_view(), name='show'),
    path('delete<int:pk>', ItemDeleteView.as_view(), name='delete'),
    ]