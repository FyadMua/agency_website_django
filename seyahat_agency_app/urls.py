
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from seyahat_agency_app import views
from seyahat_agency_app.search_forms import UserLoginForm


urlpatterns = [
    path('', views.home_page, name="home"),
    path('accounts/login/',LoginView.as_view(authentication_form=UserLoginForm),name="login_url"),
    path('register/',views.registerUser,name="register_url"),
    path('logout/',LogoutView.as_view(next_page='home'),name="logout"),
    path('accounts/profile/',views.Dashboard,name='dashboard'),
    path('package/',views.packages,name='package'),
    path('bookreservation/<int:id>/<str:title>',views.reservationBook,name='reservation'),
    path('packagebook/<str:title>/<str:date>/<int:amount>/<int:price><str:note>',views.PackageSubmit,name='packagebook'),
]
urlpatterns+= staticfiles_urlpatterns()
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
