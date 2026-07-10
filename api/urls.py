from django.urls import path, include
from .views import AccountStartView, AccountListView

urlpatterns = [
    path('start/', AccountStartView.as_view(), name='start'),
    path('accounts/', AccountListView.as_view(), name='accounts-list'),
]
