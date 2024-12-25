from django.urls import path
from . import views



app_name = 'articles'

urlpatterns = [
    path('add/', views.add_article, name='add'),
    path('category/<str:category>', views.article_category, name='category'),
    path('detail/<int:article_id>/', views.detail, name='detail'),
]

