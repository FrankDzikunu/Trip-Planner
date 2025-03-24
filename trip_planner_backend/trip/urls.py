from django.urls import path
from .views import generate_log_sheet

urlpatterns = [
    path('generate-log-sheet/', generate_log_sheet, name='generate_log_sheet'),
]
