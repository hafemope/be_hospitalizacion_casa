from urllib import request,response
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from authApp.serializers.usuarioserializer import UsuarioSerializer

class CrearUsuarioView(views.APIView):
    def post(self, request):
            serializers = UsuarioSerializer(data=request.data)
            serializers.is_valid(raise_exception=True)
            serializers.save()

            tokenData = {"username":request.data["username"],
                        "password":request.data["password"]}

            tokenSerializer = TokenObtainPairSerializer(data=tokenData)
            tokenSerializer.is_valid(raise_exception=True)

            return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED) 