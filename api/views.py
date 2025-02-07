from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from .models import Service, Project, Rate, Message, Request
from .serializers import Service_Serializer, Project_Serializer, Rate_Serializer, Message_Serializer, Request_Serializer


def custom_response(state, message, data):
    return {'state': state, 'message': message, 'data': data}


# Service Views
class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = Service_Serializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class ServiceCreateView(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = Service_Serializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [TokenAuthentication]


class ServiceUpdateView(generics.UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = Service_Serializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [TokenAuthentication]


class ServiceDeleteView(generics.DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = Service_Serializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [TokenAuthentication]


# Upload Service Picture View
class UploadServicePictureView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [TokenAuthentication]

    def post(self, request, pk, *args, **kwargs):
        service = Service.objects.get(pk=pk)
        picture = request.FILES.get('picture')
        picture_link = request.build_absolute_uri(picture.url)
        service.picture = picture
        service.save()
        return Response(custom_response(True, "Service picture uploaded successfully", picture_link), status=status.HTTP_201_CREATED)


# Project Views
class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = Project_Serializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class ProjectCreateView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = Project_Serializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [TokenAuthentication]


class ProjectUpdateView(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = Project_Serializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [TokenAuthentication]


class ProjectDeleteView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = Project_Serializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [TokenAuthentication]


# Upload Before and After Pictures Views
class ProjectUploadBeforePicturesView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [TokenAuthentication]

    def post(self, request, pk, *args, **kwargs):
        project = Project.objects.get(pk=pk)
        before_pictures = request.FILES.getlist('before_pictures')
        before_picture_links = [request.build_absolute_uri(picture.url) for picture in before_pictures]
        project.before_pictures.extend(before_picture_links)
        project.save()
        return Response(custom_response(True, "Before pictures uploaded successfully", before_picture_links), status=status.HTTP_201_CREATED)


class ProjectUploadAfterPicturesView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [TokenAuthentication]

    def post(self, request, pk, *args, **kwargs):
        project = Project.objects.get(pk=pk)
        after_pictures = request.FILES.getlist('after_pictures')
        after_picture_links = [request.build_absolute_uri(picture.url) for picture in after_pictures]
        project.after_pictures.extend(after_picture_links)
        project.save()
        return Response(custom_response(True, "After pictures uploaded successfully", after_picture_links), status=status.HTTP_201_CREATED)


# Rate Views
class RateListView(generics.ListAPIView):
    queryset = Rate.objects.all()
    serializer_class = Rate_Serializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class RateCreateView(generics.CreateAPIView):
    queryset = Rate.objects.all()
    serializer_class = Rate_Serializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class RateUpdateView(generics.UpdateAPIView):
    queryset = Rate.objects.all()
    serializer_class = Rate_Serializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [TokenAuthentication]


class RateDeleteView(generics.DestroyAPIView):
    queryset = Rate.objects.all()
    serializer_class = Rate_Serializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [TokenAuthentication]


# Message Views
class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = Message_Serializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = Message_Serializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class MessageUpdateView(generics.UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = Message_Serializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [TokenAuthentication]


class MessageDeleteView(generics.DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = Message_Serializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [TokenAuthentication]


# Request Views
class RequestListView(generics.ListAPIView):
    queryset = Request.objects.all()
    serializer_class = Request_Serializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class RequestCreateView(generics.CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = Request_Serializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class RequestUpdateView(generics.UpdateAPIView):
    queryset = Request.objects.all()
    serializer_class = Request_Serializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [TokenAuthentication]


class RequestDeleteView(generics.DestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = Request_Serializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [TokenAuthentication]


# Login View
class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            if user.is_superuser:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return Response(custom_response(True, "Login successful", {"token": token.key}), status=status.HTTP_200_OK)
            else:
                return Response(custom_response(False, "Not authorized", None), status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(custom_response(False, "Invalid credentials", None), status=status.HTTP_401_UNAUTHORIZED)
