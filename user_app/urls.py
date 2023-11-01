from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('success/', views.CheckoutSuccessView, name='success'),
    path('Failed/', views.CheckoutFailedView, name='Failed'),
    path('donation_report/', views.donation_report, name='donation_report'),
    path('account/', views.account, name='account'),
    path('account/history', views.history, name='account_history'),
    path('paypal_index/pay', views.paypal_index, name='pay_pal'),
    
    
    path('syúccess/pay', views.success, name='suc'),
    path('index/pay', views.home, name='hm'),

]
