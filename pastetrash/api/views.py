from pastes.models import Paste
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from pastes.serializers import PasteSerializer, PasteListSerializer, PasteInputSerializer

class PasteListView(generics.ListCreateAPIView):
    """
    API endpoint that list all pastes or create a new paste.
    """
    queryset = Paste.objects.all().order_by('-id')
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PasteInputSerializer
        return PasteListSerializer

class PasteSingleView(generics.RetrieveAPIView):
    """
    API endpoint to retrieve a single paste.
    """
    lookup_field = 'slug'
    queryset = Paste.objects.all()
    serializer_class = PasteSerializer

    def get_object(self):
        obj = super().get_object()
        if obj.is_protected():
            password = self.request.META.get('HTTP_X_PASSWORD', None) # TODO: Add to OpenAPI schema
            if not password:
                raise PermissionDenied('Password required')
            if obj.check_password(password) is False:
                raise PermissionDenied('Wrong password')
        return obj