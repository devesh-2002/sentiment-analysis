from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_view, name='predict_view'),
    path('predict-sentiment/', views.predict_sentiment, name='predict_sentiment'),
]

