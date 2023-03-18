from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page


# Create your views here.

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT) #Caching-Time defined in settings.py or DEFAULT_TIMEOUT

@login_required(login_url='/login/') #videos is only accessible if logged in, otherwise you will get redirected to login
@cache_page(CACHE_TTL) #Endpoint will be cached and therefore is loading faster
def videos_view(request):
 """
  This is a view that allows videos to be viewed
 """
 return render(request, 'videos/videos.html')