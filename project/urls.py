from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from api.views import (ServiceListView, ServiceCreateView, ServiceUpdateView, ServiceDeleteView,
                    ProjectListView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView,
                    ProjectUploadBeforePicturesView, ProjectUploadAfterPicturesView,
                    RateListView, RateCreateView, RateUpdateView, RateDeleteView,
                    MessageListView, MessageCreateView, MessageUpdateView, MessageDeleteView,
                    RequestListView, RequestCreateView, RequestUpdateView, RequestDeleteView,
                    LoginView, UploadServicePictureView)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Service URLs
    path('api/services/', ServiceListView.as_view(), name='service-list'),
    path('api/services/create/', ServiceCreateView.as_view(), name='service-create'),
    path('api/services/<int:pk>/update/', ServiceUpdateView.as_view(), name='service-update'),
    path('api/services/<int:pk>/delete/', ServiceDeleteView.as_view(), name='service-delete'),
    path('api/services/<int:pk>/upload-picture/', UploadServicePictureView.as_view(), name='service-upload-picture'),

    # Project URLs
    path('api/projects/', ProjectListView.as_view(), name='project-list'),
    path('api/projects/create/', ProjectCreateView.as_view(), name='project-create'),
    path('api/projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('api/projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    path('api/projects/<int:pk>/upload-before-pictures/', ProjectUploadBeforePicturesView.as_view(), name='project-upload-before-pictures'),
    path('api/projects/<int:pk>/upload-after-pictures/', ProjectUploadAfterPicturesView.as_view(), name='project-upload-after-pictures'),

    # Rate URLs
    path('api/rates/', RateListView.as_view(), name='rate-list'),
    path('api/rates/create/', RateCreateView.as_view(), name='rate-create'),
    path('api/rates/<int:pk>/update/', RateUpdateView.as_view(), name='rate-update'),
    path('api/rates/<int:pk>/delete/', RateDeleteView.as_view(), name='rate-delete'),

    # Message URLs
    path('api/messages/', MessageListView.as_view(), name='message-list'),
    path('api/messages/create/', MessageCreateView.as_view(), name='message-create'),
    path('api/messages/<int:pk>/update/', MessageUpdateView.as_view(), name='message-update'),
    path('api/messages/<int:pk>/delete/', MessageDeleteView.as_view(), name='message-delete'),

    # Request URLs
    path('api/requests/', RequestListView.as_view(), name='request-list'),
    path('api/requests/create/', RequestCreateView.as_view(), name='request-create'),
    path('api/requests/<int:pk>/update/', RequestUpdateView.as_view(), name='request-update'),
    path('api/requests/<int:pk>/delete/', RequestDeleteView.as_view(), name='request-delete'),

    # Login URL
    path('api/login/', LoginView.as_view(), name='login'),

    # Upload Service Picture URL
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]
