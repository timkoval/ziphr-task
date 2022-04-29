from django.urls import include, path
from rest_framework import routers
from planes import views

router = routers.DefaultRouter()
router.register(r'planes', views.PlaneViewSet)
router.register(r'passengers', views.PassengerViewSet)

# Wire our API using automatic URL routing.
# Moreover, we can include login URLs for browsable APIs.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
