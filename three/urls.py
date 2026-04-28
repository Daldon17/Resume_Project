from django.urls import path
from . import views

app_name = 'three'

urlpatterns = [
    path('', views.upload_resume, name='upload'),

    # NEW
    path('templates/', views.select_template, name='select_template'),
    path('create/<str:template_name>/', views.create_resume, name='create_resume'),
    path('preview/', views.preview_resume, name='preview_resume'),
    path('download/', views.download_resume, name='download_resume'),

    # ===== NEW API CODE START =====
    path('api', views.api_root),
    path('api/', views.api_root, name='api_root'),
    path('api/health', views.api_health),
    path('api/health/', views.api_health, name='api_health'),
    path('api/upload-resume', views.api_upload_resume),
    path('api/upload-resume/', views.api_upload_resume, name='api_upload_resume'),
    path('api/analyze', views.api_analyze_resume),
    path('api/analyze/', views.api_analyze_resume, name='api_analyze_resume'),
    path('api/results/<int:id>', views.api_resume_results),
    path('api/results/<int:id>/', views.api_resume_results, name='api_resume_results'),
    path('api/templates', views.api_resume_templates),
    path('api/templates/', views.api_resume_templates, name='api_resume_templates'),
    # ===== NEW API CODE END =====
]
