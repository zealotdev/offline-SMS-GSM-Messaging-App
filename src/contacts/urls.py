from django.urls import path


from contacts import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contactslist/', views.ContactListView.as_view(), name='contacts_list'),
    path('category/', views.CategoryListView.as_view(), name='category'),
    path('category/<int:pk>', views.CategoryDetailVew.as_view(),
         name='category-detail'),
    path('add_contact/', views.AddContactView.as_view(), name='add_contact'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('sendsms/', views.SendSMSView.as_view(), name='sendsms'),
    path('history/', views.HistoryView.as_view(), name='history')


]
