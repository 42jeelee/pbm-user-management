from django.urls import path, include
from . import views

urlpatterns = [
	path('google/login/', views.SocialLogin.as_view(), name='google_login'),
	path('42intra/login/', views.SocialLogin.as_view(), name='42intra_login'),
	path('google/login/callback/', views.SocialLoginCallBack.as_view(), name='google_callback'),
	path('42intra/login/callback/', views.SocialLoginCallBack.as_view(), name='intra_callback'),
]
