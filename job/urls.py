from django.urls import path

from . import views

urlpatterns = [
    path('position/', views.PositionListCreateAPIView.as_view()),
    path('employee/', views.EmployeeListCreateAPIView.as_view()),

]