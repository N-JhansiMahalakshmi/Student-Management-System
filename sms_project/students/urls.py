# from django.urls import path
# from . import views

# urlpatterns = [

#     # Main Pages
#     path('', views.dashboard, name='dashboard'),
#     path('about/', views.about, name='about'),

#     # Student Management
#     path('students/', views.student_list, name='student_list'),
#     path('students/add/', views.add_student, name='add_student'),
#     path('students/edit/<int:id>/', views.edit_student, name='edit_student'),
#     path('students/detail/<int:id>/', views.student_detail, name='student_detail'),
#     path('students/delete/<int:id>/', views.delete_student, name='delete_student'),

#     # Short aliases for the same student pages.
#     path('add/', views.add_student),
#     path('edit/<int:id>/', views.edit_student),
#     path('detail/<int:id>/', views.student_detail),
#     path('delete/<int:id>/', views.delete_student),

#     # Compatibility Routes
#     path('dashboard.html', views.dashboard),
#     path('student_list.html', views.student_list),
#     path('students/student_list.html', views.student_list),
#     path('add_student.html', views.add_student),
#     path('students/add_student.html', views.add_student),
#     path('edit_student.html', views.edit_student_query),
#     path('students/edit_student.html', views.edit_student_query),
#     path('student_detail.html', views.student_detail_query),
#     path('students/student_detail.html', views.student_detail_query),
#     path('delete_student.html', views.delete_student_query),
#     path('students/delete_student.html', views.delete_student_query),
#     path('about.html', views.about),
#     path('students/about.html', views.about),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('students/', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('detail/<int:id>/', views.student_detail, name='student_detail'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    path('about/', views.about, name='about'),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('edit/<int:id>/',views.edit_student,name='edit_student'),
    path('export/pdf/',views.export_students_pdf,name='export_students_pdf'),
]