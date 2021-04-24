from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('comment-list/', views.commentList, name="comment-list"),
	path('comment-detail/<str:pk>/', views.commentDetail, name="comment-detail"),
	path('comment-create/', views.commentCreate, name="comment-create"),
	path('differentiate/', views.differentiate, name="differentiate"),
]
