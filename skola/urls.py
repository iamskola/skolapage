from django.urls import path
from .views import home_view, about_view, contact_view, testimonial_view, product_view, add_review

urlpatterns=[
    path("", home_view, name='home'),
    path('about/', about_view, name='about us'),
    path('contact us/', contact_view, name='contact'),
    path('testimonial/', testimonial_view, name='testimony'),
    path('our_products/', product_view, name='products'),
    path('add_review/', add_review, name='add_review'),
    #path('post/<int:post_id>/', delete_post, name='delete-post'),
    #path('post/<int:post_id>/edit/', edit_post, name='edit-post'),
]
