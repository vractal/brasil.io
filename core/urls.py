from django.urls import path

from . import views, views_special


app_name = 'core'
urlpatterns = [
    # Institutional pages
    path('', views.index, name='index'),
    path('contato', views.contact, name='contact'),
    path('datasets', views.dataset_list, name='dataset-list'),
    path('dataset/<slug>', views.dataset_detail, name='dataset-detail'),
    path('datasets/sugira', views.dataset_suggestion, name='dataset-suggestion'),
    path('manifesto', views.manifesto, name='manifesto'),

    # Dataset-specific pages (specials)
    path('especiais/empresas', views_special.companies, name='special-companies'),
    path('especiais/empresa/<document>', views_special.company_detail, name='special-company-detail'),
]
