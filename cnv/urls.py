from django.urls import path
from .views import CnvView, CnvNew

urlpatterns = [
	path('cnv/',CnvView.as_view(), name='cnv_list'),
	path('nuevo/',CnvNew.as_view(), name='cnv_new')
]