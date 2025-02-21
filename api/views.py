from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from .models import Service, Project, Rate, Message, Request
from .serializers import Service_Serializer, Project_Serializer, Rate_Serializer, Message_Serializer, Request_Serializer
from django.core.files.storage import default_storage
from django.conf import settings
import os
from django.core.files.storage import default_storage
from django.conf import settings


def index(request):
    return render(request, "index.html")


def custom_response(state, message, data):
    return {'state': state, 'message': message, 'data': data}


# Service Views
class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = Service_Serializer


class ServiceCreateView(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = Service_Serializer
#    permission_classes = [permissions.IsAdminUser]
#    authentication_classes = [TokenAuthentication]


class ServiceUpdateView(generics.UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = Service_Serializer
#    permission_classes = [permissions.IsAdminUser]
#    authentication_classes = [TokenAuthentication]


class ServiceDeleteView(generics.DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = Service_Serializer
#    permission_classes = [permissions.IsAdminUser]
#    authentication_classes = [TokenAuthentication]


# Upload Service Picture View
class UploadServicePictureView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, pk, *args, **kwargs):
        service = Service.objects.get(pk=pk)
        picture = request.FILES.get('picture')

        if not picture:
            return Response(custom_response(False, "No picture provided", None), status=status.HTTP_400_BAD_REQUEST)

        # Save the file to the default storage
        file_path = default_storage.save(f'service_pictures/{picture.name}', picture)
        picture_url = f"{settings.MEDIA_URL}{file_path}"

        service.picture = file_path
        service.save()

        return Response(custom_response(True, "Service picture uploaded successfully", request.build_absolute_uri(picture_url)), status=status.HTTP_201_CREATED)


# Project Views
class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = Project_Serializer
#    permission_classes = [permissions.IsAuthenticated]
#    authentication_classes = [TokenAuthentication]


class ProjectCreateView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = Project_Serializer
#    permission_classes = [permissions.IsAdminUser]
#    authentication_classes = [TokenAuthentication]


class ProjectUpdateView(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = Project_Serializer
#    permission_classes = [permissions.IsAdminUser]
#    authentication_classes = [TokenAuthentication]


class ProjectDeleteView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = Project_Serializer

    def delete(self, request, *args, **kwargs):
        project = self.get_object()

        # حذف الصور المرتبطة بالمشروع من التخزين
        def delete_images(image_list):
            if image_list:
                for image_url in image_list:
                    # استخراج المسار الفعلي للملف من `MEDIA_ROOT`
                    relative_path = image_url.replace(request.build_absolute_uri(settings.MEDIA_URL), "")
                    file_path = os.path.join(settings.MEDIA_ROOT, relative_path)

                    # حذف الملف إن وجد
                    if os.path.exists(file_path):
                        os.remove(file_path)

        delete_images(project.before_pictures)
        delete_images(project.after_pictures)

        # حذف المشروع بعد حذف الصور
        response = super().delete(request, *args, **kwargs)
        return Response(custom_response(True, "Project and its images deleted successfully", None), status=status.HTTP_200_OK)


# Upload Before and After Pictures Views
class ProjectUploadBeforePicturesView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, pk, *args, **kwargs):
        project = Project.objects.get(pk=pk)
        before_pictures = request.FILES.getlist('before_pictures')

        if not before_pictures:
            return Response(custom_response(False, "No before pictures provided", None), status=status.HTTP_400_BAD_REQUEST)

        before_picture_links = project.before_pictures if project.before_pictures else []  # تحميل القائمة الحالية

        for picture in before_pictures:
            file_path = default_storage.save(f'project_pictures/before/{picture.name}', picture)
            picture_url = request.build_absolute_uri(f"{settings.MEDIA_URL}{file_path}")
            before_picture_links.append(picture_url)  # إضافة الصورة الجديدة للقائمة

        project.before_pictures = before_picture_links  # تحديث القائمة في قاعدة البيانات
        project.save()

        return Response(custom_response(True, "Before pictures uploaded successfully", before_picture_links), status=status.HTTP_201_CREATED)


class ProjectUploadAfterPicturesView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, pk, *args, **kwargs):
        project = Project.objects.get(pk=pk)
        after_pictures = request.FILES.getlist('after_pictures')

        if not after_pictures:
            return Response(custom_response(False, "No after pictures provided", None), status=status.HTTP_400_BAD_REQUEST)

        after_picture_links = project.after_pictures if project.after_pictures else []  # تحميل القائمة الحالية

        for picture in after_pictures:
            file_path = default_storage.save(f'project_pictures/after/{picture.name}', picture)
            picture_url = request.build_absolute_uri(f"{settings.MEDIA_URL}{file_path}")
            after_picture_links.append(picture_url)  # إضافة الصورة الجديدة للقائمة

        project.after_pictures = after_picture_links  # تحديث القائمة في قاعدة البيانات
        project.save()

        return Response(custom_response(True, "After pictures uploaded successfully", after_picture_links), status=status.HTTP_201_CREATED)


# Rate Views
class RateListView(generics.ListAPIView):
    queryset = Rate.objects.filter(state=True)  # Only get rates where state=True
    serializer_class = Rate_Serializer


class RateListAllView(generics.ListAPIView):
    queryset = Rate.objects.all()
    serializer_class = Rate_Serializer
#    permission_classes = [permissions.IsAuthenticated]
#    authentication_classes = [TokenAuthentication]


class RateCreateView(generics.CreateAPIView):
    queryset = Rate.objects.all()
    serializer_class = Rate_Serializer
#    permission_classes = [permissions.IsAuthenticated]
#    authentication_classes = [TokenAuthentication]


class RateUpdateView(generics.UpdateAPIView):
    queryset = Rate.objects.all()
    serializer_class = Rate_Serializer
#    permission_classes = [permissions.IsAdminUser]
#    authentication_classes = [TokenAuthentication]


class RateDeleteView(generics.DestroyAPIView):
    queryset = Rate.objects.all()
    serializer_class = Rate_Serializer
#    permission_classes = [permissions.IsAdminUser]
#    authentication_classes = [TokenAuthentication]


# Message Views
class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = Message_Serializer
#    permission_classes = [permissions.IsAuthenticated]
#    authentication_classes = [TokenAuthentication]


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = Message_Serializer
#    permission_classes = [permissions.IsAuthenticated]
#    authentication_classes = [TokenAuthentication]


class MessageUpdateView(generics.UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = Message_Serializer
#    permission_classes = [permissions.IsAdminUser]
#    authentication_classes = [TokenAuthentication]


class MessageDeleteView(generics.DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = Message_Serializer
#    permission_classes = [permissions.IsAdminUser]
#    authentication_classes = [TokenAuthentication]


# Request Views
class RequestListView(generics.ListAPIView):
    queryset = Request.objects.all()
    serializer_class = Request_Serializer
#    permission_classes = [permissions.IsAuthenticated]
#    authentication_classes = [TokenAuthentication]


class RequestCreateView(generics.CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = Request_Serializer
#    permission_classes = [permissions.IsAuthenticated]
#    authentication_classes = [TokenAuthentication]


class RequestUpdateView(generics.UpdateAPIView):
    queryset = Request.objects.all()
    serializer_class = Request_Serializer
#    permission_classes = [permissions.IsAdminUser]
#    authentication_classes = [TokenAuthentication]


class RequestDeleteView(generics.DestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = Request_Serializer
#    permission_classes = [permissions.IsAdminUser]
#    authentication_classes = [TokenAuthentication]


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
