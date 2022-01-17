from django.urls import path
from fileapp import views as fileapp_views


urlpatterns = [
    path('upload/', fileapp_views.FileParserView.as_view(), name='fileupload'),
    path('upload/update-file/', fileapp_views.FileUpdateParserView.as_view(), name='fileupdate'),
]
