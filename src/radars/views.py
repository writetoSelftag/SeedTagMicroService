import json

from rest_framework import viewsets, status
from rest_framework.response import Response

from src.radars.models import RadarInput
from src.radars.serializers import RadarSerializer


class RadarViewSet(viewsets.ViewSet):

    def scan(self, request):  # /radar
        scanner = RadarInput(request.data["protocols"], request.data["scan"])
        response = scanner.get_coords()
        radar = {
            "input": json.dumps(request.data),
            "response": json.dumps(response)
        }
        serializer = RadarSerializer(data=radar)
        serializer.is_valid(raise_exception=True)

        #serializer.save()
        return Response(response, status=status.HTTP_200_OK)
