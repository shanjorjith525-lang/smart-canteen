from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_list, name='food_list'),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('dashboard/', views.customer_dashboard, name='customer_dashboard'),

    path('analytics/', views.analytics_dashboard, name='analytics_dashboard'),

    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('date-report/', views.date_report, name='date_report'),
    path('pdf-report/', views.pdf_report, name='pdf_report'),
    path('excel-report/', views.excel_report, name='excel_report'),

    path(
        'period-analytics/',
        views.period_analytics,
        name='period_analytics'
    ),

    path(
        'demand-prediction/',
        views.demand_prediction,
        name='demand_prediction'
    ),

    path(
        'waste-analysis/',
        views.waste_analysis,
        name='waste_analysis'
    ),

    path(
        'order/<int:food_id>/',
        views.order_food,
        name='order_food'
    ),

    path(
        'my-orders/',
        views.my_orders,
        name='my_orders'
    ),

    path(
        'order-status/<int:order_id>/',
        views.order_status,
        name='order_status'
    ),
]