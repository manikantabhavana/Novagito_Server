from django.urls import path
from .views import customer_list,testinominal_list,query_list

urlpatterns = [
    path('customers/', customer_list, name='customer-list'),
    path('testinominals/', testinominal_list, name='testinominal-list'),
    path('query/', query_list, name='query-list'),
   
]
