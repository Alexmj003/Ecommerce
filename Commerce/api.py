from rest_framework import routers
from polls import views as my_views

router = routers.DefaultRouter()
router.register(r'Business',my_views.BusinessViewset)
router.register(r'Employee',my_views.EmployeeViewset)
router.register(r'Employed',my_views.EmployedViewset)