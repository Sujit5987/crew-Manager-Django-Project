from django.contrib import admin
from django.urls import path,include
from employee.views import *
from django.contrib import admin
from django.urls import path
from employee.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('indexemployee/',indexemployee,name="indexemployee"),
    path('delete/<int:id>/',delete,name='delete'),
    path('update/<int:id>/',update,name='update'),
    path('home/serch/',serch,name="serch"),
    path('home/',home,name="home"),
    path('home/home/',home,name="home"),
    path('home/indexemployee/',indexemployee,name="indexemployee"),
    path('home/home/add/',add,name="add"),
    path('signup/',signup,name="signup"),
    path('login/',login,name="login"),
    path('login/signup/',signup,name="signup"),
    path('home/signup/',signup,name="signup"),
    path('home/login/',login,name="login"),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns +=staticfiles_urlpatterns()
