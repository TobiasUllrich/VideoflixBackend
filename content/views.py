from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from rest_framework.authtoken.views import ObtainAuthToken 
from rest_framework.authtoken.models import Token 
from rest_framework.response import Response 
from .serializers import UsersSerializer

# Create your views here.

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT) #Caching-Time defined in settings.py or DEFAULT_TIMEOUT

@login_required(login_url='/login/') #videos is only accessible if logged in, otherwise you will get redirected to login
@cache_page(CACHE_TTL) #Endpoint will be cached and therefore is loading faster
def videos_view(request):
 """
  This is a view that allows videos to be viewed
 """
 return render(request, 'videos/videos.html')

class LoginView(ObtainAuthToken): 
 def post(self, request, *args, **kwargs): 
  serializer = self.serializer_class(data=request.data, context={'request': request}) 
  serializer.is_valid(raise_exception=True) 
  user = serializer.validated_data['user'] 
  token, created = Token.objects.get_or_create(user=user) 
  return Response({ 'token': token.key, 'user_id': user.pk, 'email': user.email })
