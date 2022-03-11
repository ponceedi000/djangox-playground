from django.urls import path
from .views import PlayGroundListView, PlayGroundDetailView, PlayGroundCreateView, PlayGroundUpdateView, PlayGroundDeleteView

urlpatterns = [
    path('', PlayGroundListView.as_view(), name='play_ground_list'),
    path('<int:pk>/', PlayGroundDetailView.as_view(), name='play_ground_detail'),
    path('create/', PlayGroundCreateView.as_view(), name='play_ground_create'),
    path('<int:pk>/update/', PlayGroundUpdateView.as_view(), name='play_ground_update'),
    path('<int:pk>/delete/', PlayGroundDeleteView.as_view(), name='play_ground_delete'),
]