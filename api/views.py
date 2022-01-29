from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime




@api_view(['Get'])
def index(request):
    message = 'server is live current time is'
    return Response(message + datetime.now().strftime("%d/%m/%Y /%H:%M:%S"), status=status.HTTP_200_OK)