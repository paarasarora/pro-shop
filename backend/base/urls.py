from django.urls import path
from . import views



urlpatterns = [
    path('user/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('',views.api_views.as_view(),name = 'api-view'),
    path('<str:id>/',views.api_view_single.as_view(),name = 'api-single'),
    path('user/profile/',views.getUserProfile,name = 'user')
]
