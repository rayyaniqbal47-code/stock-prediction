from django.urls import path
from accounts import views as UserViews
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView
from . import views

urlpatterns = [
    path('register/' , UserViews.RegisterView.as_view() , name='register'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('ProtectedView/', UserViews.ProtectedView.as_view(), name='ProtectedView'),


    # stock api

    path('predict/', views.StockAPIView.as_view(), name='predict'),


]



