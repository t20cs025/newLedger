from django.urls import path
from .views import ItemList, ItemEditView,ItemShowView,ItemDeleteView,ItemAddView
from .views import ItemMainView,LoginView,SignUpView,RegisterView,DocumentView,ApprovalView
from .views import LedgerList

app_name = 'shoppinglist'
urlpatterns = [
    path('list/',LedgerList.as_view(),name='list'),
#     path('list/',ItemList.as_view(),name='list'),
    path('add', ItemAddView.as_view(), name='add'),
    
    path('edit/<int:pk>', ItemEditView.as_view(),name='edit'),

    path('show', ItemShowView.as_view(), name='show'),
    path('delete<int:pk>', ItemDeleteView.as_view(), name='delete'),
    path('main',ItemMainView.as_view(),name='main'),
    path('login',LoginView.as_view(),name='login'),
    path('signup',SignUpView.as_view(),name='signup'),
    path('register',RegisterView.as_view(),name='register'),
    path('approval',ApprovalView.as_view(),name='approval'),
    path('document',DocumentView.as_view(),name='document'),
    ]