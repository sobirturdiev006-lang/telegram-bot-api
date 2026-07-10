from django.urls import path, include
from .views import AccountStartView, AccountListView, AccountDetailView

urlpatterns = [
    path('start/', AccountStartView.as_view(), name='start'),
    path('accounts/', AccountListView.as_view(), name='accounts-list'),
    path('accounts/<int:telegram_id>/', AccountDetailView.as_view(), name='accounts-detail'),
]
