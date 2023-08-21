from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from api import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('pastes', views.PasteListView.as_view(), name='paste-list'),
    path('pastes/<slug:slug>', views.PasteSingleView.as_view(), name='paste-single'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # OpenAPI schema
    path('openapi', get_schema_view(
        title="Pastetrash API",
        description="API for pastetrash",
        version="1.0.0"
    ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]