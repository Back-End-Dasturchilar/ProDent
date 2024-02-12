from django.urls import path
from .views import ContactAPIView, ContactNextAPIView

urlpatterns = [
    path('', ContactAPIView.as_view(), name='Contact_API_View'),
    path('next/', ContactNextAPIView.as_view(), name='ContactNext_API_View'),

]
