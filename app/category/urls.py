from django.urls import path

from app.category.views import CategoryListView, CategoryDetailView

urlpatterns = [
    path('category-list/', CategoryListView.as_view()),
    # path('category-list/<int:pk>/', CategoryDetailView.as_view()),
]
