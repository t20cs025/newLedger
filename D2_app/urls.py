from django.urls import path
from .views import Ledger
from .views import MainView,LoginView,SignUpView,RegisterView,DocumentView,ApprovalView
from .views import LedgerList

app_name='D2_app'
urlpatterns = [
    path('main/',MainView.as_view(),name='main'),
    path('list/',Ledger.as_view(),name='list'),
    path('login',LoginView.as_view(),name='login'),
    path('signup',SignUpView.as_view(),name='signup'),
    path('register',RegisterView.as_view(),name='register'),
    path('ledger_list',LedgerList.as_view(),name='ledger_list'),
    path('approval',ApprovalView.as_view(),name='approval'),
    path('document',DocumentView.as_view(),name='document'),
]