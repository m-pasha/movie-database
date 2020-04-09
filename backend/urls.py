from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from app.views import HomeView, LoginView, SearchView, FavouriteView

urlpatterns = [

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('search/', SearchView.as_view(), name='search'),
    path('favourite/', FavouriteView.as_view(), name='favourite'),

    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
