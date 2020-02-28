from rest_framework import viewsets
from .models import Essay
# from .serializers import Essayserializers

class PostViewSet(viewsets.ModelViewSet):
    queryset = Essay.objects.all()
    # serializer_class = Essayserializers

