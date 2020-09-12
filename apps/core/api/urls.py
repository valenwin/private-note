from django.urls import path

from apps.core.api import views as api_views

urlpatterns = [
    path('create-message/', api_views.create_message, name='create-message'),
    path(
        'get-message/<int:message_id>/<str:access_token>/',
        api_views.get_message,
        name='get-message'),

]
