from django import urls
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('posts', views.Posts.as_view(), name='posts'),
    path('posts/<slug:slug>', views.Post.as_view(), name='post'),
    path('contact', views.Contact.as_view(), name='contact'),
    path('donate', views.Donate.as_view(), name='donate')
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)