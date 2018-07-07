from django.conf.urls import url
from Gapp import views as G_views

urlpatterns = [
	url(r'home/$', G_views.home,name='home'),
	url(r'article/$', G_views.ArticleView,name='article'),
	url(r'activity/$', G_views.ActivityData,name='activity'),
	url(r'announce/$', G_views.AnnounceView,name='announce'),
	url(r'announcementss/$', G_views.AnnouncementView,name='announcementss'),
    
]