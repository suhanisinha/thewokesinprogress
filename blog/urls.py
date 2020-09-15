from django.urls import path
from .views import HomeView, MyProfileView, FullArticleView, NewArticleView, EditArticleView, DeleteArticleView, \
    AddCategoryView, CategoryView, LikeView, EditMyProfileView

urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('my_profile/', MyProfileView.as_view(), name='my-profile'),
    path('article/<int:pk>', FullArticleView.as_view(), name='full-article'),
    path('new_article/', NewArticleView.as_view(), name='new-article'),
    path('add_category/', AddCategoryView.as_view(), name='add-category'),
    path('article/edit/<int:pk>', EditArticleView.as_view(), name='edit-article'),
    path('my_profile/edit/<int:pk>', EditMyProfileView.as_view(), name='edit-myprofile'),
    path('article/<int:pk>/delete', DeleteArticleView.as_view(), name='delete-article'),
    path('category/<str:cat>/', CategoryView, name='category'),
    path('like/<int:pk>/', LikeView, name='like'),

]
