from django.urls import path
from . import views

urlpatterns = [

    # 🔐 Auth
    path('', views.login_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # 📊 Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # 📋 Leads
    path('leads/', views.leads, name='leads'),
    path('lead/<int:id>/', views.view_lead, name='view_lead'),
    path('add-lead/', views.add_lead, name='add_lead'),
    path('edit-lead/<int:id>/', views.edit_lead, name='edit_lead'),
    path('delete-lead/<int:id>/', views.delete_lead, name='delete_lead'),
    path('lead/<int:id>/convert/', views.convert_to_customer, name='convert_to_customer'),

    # 📂 Import
    path('import/', views.import_data, name='import_data'),

    # 👥 Customers
    path('customers/', views.customers, name='customers'),
    path('customers/add/', views.add_customer, name='add_customer'),
    path('customers/<int:id>/view/', views.view_customer, name='view_customer'),
    path('customers/<int:id>/edit/', views.edit_customer, name='edit_customer'),
    path('customers/<int:id>/delete/', views.delete_customer, name='delete_customer'),

    # 🏗️ Projects
    path('projects/', views.projects, name='projects'),
    path('projects/add/', views.add_project, name='add_project'),
    path('projects/<int:id>/view/', views.view_project, name='view_project'),
    path('projects/<int:id>/edit/', views.edit_project, name='edit_project'),
    path('projects/<int:id>/delete/', views.delete_project, name='delete_project'),

    # 📄 Quotes
    path('quotes/', views.quotes, name='quotes'),
    path('quotes/add/', views.add_quote, name='add_quote'),
    path('quotes/<int:id>/view/', views.view_quote, name='view_quote'),
    path('quotes/<int:id>/edit/', views.edit_quote, name='edit_quote'),
    path('quotes/<int:id>/delete/', views.delete_quote, name='delete_quote'),

    # 🧾 Invoices
    path('invoices/', views.invoices, name='invoices'),
    path('invoices/add/', views.add_invoice, name='add_invoice'),
    path('invoices/<int:id>/view/', views.view_invoice, name='view_invoice'),
    path('invoices/<int:id>/delete/', views.delete_invoice, name='delete_invoice'),


    # 📞 Follow Ups
    path('followups/', views.followups, name='followups'),
    path('followups/add/', views.add_followup, name='add_followup'),
    path('followups/<int:id>/view/', views.view_followup, name='view_followup'),
    path('followups/<int:id>/edit/', views.edit_followup, name='edit_followup'),
    path('followups/<int:id>/toggle/', views.toggle_followup, name='toggle_followup'),
    path('followups/<int:id>/delete/', views.delete_followup, name='delete_followup'),

    # 👥 Employees
    path('employees/', views.employees, name='employees'),
    path('employees/add/', views.add_employee, name='add_employee'),
    path('employees/<int:id>/delete/', views.delete_employee, name='delete_employee'),

    # 🔑 Forgot Password
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('verify-reset-otp/', views.verify_reset_otp, name='verify_reset_otp'),
    path('reset-password/', views.reset_password, name='reset_password'),

    # ================= AJAX =================
    path('ajax/dashboard-stats/', views.ajax_dashboard_stats, name='ajax_dashboard_stats'),
    path('ajax/lead/<int:id>/status/', views.ajax_change_lead_status, name='ajax_change_lead_status'),
    path('ajax/lead/<int:id>/delete/', views.ajax_delete_lead, name='ajax_delete_lead'),
    path('ajax/lead/add/', views.ajax_add_lead, name='ajax_add_lead'),
    path('ajax/notifications/', views.ajax_notifications, name='ajax_notifications'),
    path('ajax/search/', views.ajax_live_search, name='ajax_live_search'),
]