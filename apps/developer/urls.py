"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from apps.developer import views

urlpatterns = [
    path('', views.main_page),
    path('update-ranking', views.save_tech_ranking_data),
    path('update-git-rainbow', views.update_git_rainbow),
    path('leaderboards', views.leaderboards_tech_stack),
    path('leaderboards/<str:tech_name>', views.leaderboards_tech_stack),
    path('<str:github_id>', views.git_rainbow),
    path('svg/<str:github_id>', views.git_rainbow_svg)
]
