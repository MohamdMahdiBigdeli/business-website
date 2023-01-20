from django.contrib import admin
from django.urls import path
from controller.API import about_data, blog_data, brand_logo_data, call_to_action_data, features_data, funfact_data, \
    how_we_works_data, navbar_data, pricing_table_data, services_data, sidebar_data, slider_data, social_networks_data, \
    team_data, testimonial_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about-data/', about_data),
    path('brand-logo-data/', brand_logo_data),
    path('blog-data/', blog_data),
    path('call-to-action-data/', call_to_action_data),
    path('features-data/', features_data),
    path('funfact-data/', funfact_data),
    path('how-we-works-data/', how_we_works_data),
    path('navbar-data/', navbar_data),
    path('pricing-table-data/', pricing_table_data),
    path('services-data/', services_data),
    path('sidebar-data/', sidebar_data),
    path('slider-data/', slider_data),
    path('social-networks-data/', social_networks_data),
    path('team-data/', team_data),
    path('testimonial-data/', testimonial_data),
]

