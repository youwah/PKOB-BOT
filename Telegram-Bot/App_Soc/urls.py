from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.student),
    path('lecturer/', views.lecturer),
    path('student_report/', views.student_report),
    path('homepage/', views.home, name='home'),
    path('student_data/', views.index, name='data'),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    path('add/', views.my_form, name='form')
   # path('<int:question_id>/', views.detail, name='detail'),
]

#url(r'form', views.my_form, name='form')
#{% if latest_question_list %}
#    <ul>
#    {% for question in latest_question_list %}
#        <li><a href="/App_Soc/{{ question.id }}/">{{ question.name_text }}</a></li>
#        <li><a href="/App_Soc/{{ question.id }}/">{{ question.ic_text }}</a></li>
#        <li><a href="/App_Soc/{{ question.id }}/">{{ question.phone_text }}</a></li>
#    {% endfor %}
#    </ul>
#{% else %}
#    <p>No details are available.</p>
#{% endif %}