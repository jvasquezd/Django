"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.homepage.views import IndexView
from core.login.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', include('core.login.urls')),
    path('admin/', admin.site.urls),
    path('erp/', include('core.erp.urls')),
    path('reports/', include('core.reports.urls')),
    path('user/', include('core.user.urls')),
]

"""
Administrar archivos estáticos (por ejemplo, imágenes, JavaScript, CSS)
Los sitios web generalmente necesitan entregar archivos adicionales como imágenes, 
JavaScript o CSS. En Django, nos referimos a estos archivos como "archivos estáticos". 
Django proporciona django.contrib.staticfiles para ayudarlo a administrarlos.

Configurando Archivos Estaticos
1. Asegurese de que django.contrib.staticfiles este incluido en INSTALLED_APPS.
2. En su archivo de configuración, defina STATIC_URL, por ejemplo:
    STATIC_URL = '/static/'
3. En sus plantillas, use la static etiqueta de plantilla para crear la URL para 
la ruta relativa dada usando el archivo STATICFILES_STORAGE.
4. Almacene sus archivos estáticos en una carpeta llamada staticen su aplicación.
 Por ejemplo my_app/static/my_app/example.jpg.
 

Sirviendo archivos estáticos durante el desarrollo
Si usa django.contrib.staticfiles como se explicó anteriormente, runserverlo hará automáticamente cuando DEBUG
esté configurado en True. Si usted no tiene django.contrib.staticfiles en INSTALLED_APPS, todavía puede servir 
archivos estáticos manualmente utilizando la vista django.views.static.serve() 

¡Esto no es adecuado para uso de producción! Para conocer algunas estrategias de implementación comunes, consulte
Implementación de archivos estáticos.

Por ejemplo, si tu STATIC_URL se define como /static/, puedes hacer esto agregando el siguiente fragmento a tu urls.py:
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

Entrega de archivos cargados por un usuario durante el desarrollo
Durante el desarrollo, puede servir archivos multimedia cargados por el usuario desde MEDIA_ROOT 
la vista django.views.static.serve().

¡Esto no es adecuado para uso de producción! Para conocer algunas estrategias de implementación comunes,
consulte Implementación de archivos estáticos .

Por ejemplo, si tu MEDIA_URLse define como /media/, puedes hacer esto agregando el siguiente fragmento a tu urls.py:
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
