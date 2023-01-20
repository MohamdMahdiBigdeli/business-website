from rest_framework.decorators import api_view
from django.http import HttpResponse
import json
from controller.about import about
from controller.blog import blog
from controller.brandLogo import brand_logo
from controller.callToAction import call_to_actiondata
from controller.features import features
from controller.funfact import funfact
from controller.howWeWorks import how_we_works
from controller.pricingTable import pricing_table
from controller.services import services
from controller.sidebar import sidebar
from controller.slider import slider
from controller.socialNetworks import social_networks
from controller.team import team
from controller.testimonials import testimonials


@api_view(['''GET'''])
def about_data(request):
    return HttpResponse(json.dumps(about()), content_type='application/json')


@api_view(['''GET'''])
def blog_data(request):
    return HttpResponse(json.dumps(blog()), content_type='application/json')


@api_view(['''GET'''])
def brand_logo_data(request):
    return HttpResponse(json.dumps(brand_logo()), content_type='application/json')


@api_view(['''GET'''])
def call_to_action_data(request):
    return HttpResponse(json.dumps(call_to_actiondata()), content_type='application/json')


@api_view(['''GET'''])
def features_data(request):
    return HttpResponse(json.dumps(features()), content_type='application/json')


@api_view(['''GET'''])
def funfact_data(request):
    return HttpResponse(json.dumps(funfact()), content_type='application/json')


@api_view(['''GET'''])
def how_we_works_data(request):
    return HttpResponse(json.dumps(how_we_works()), content_type='application/json')


@api_view(['''GET'''])
def navbar_data(request):
    data = [
  {
    "id": 1,
    "title": "خانه",
    "link": "/",
    "megaMenu": False,
    "subMenu": [
      {
        "id": 1.1,
        "title": "خانه 1",
        "link": "/home-one"
      },
      {
        "id": 1.2,
        "title": "خانه 2",
        "link": "/home-two"
      }
    ]
  },
  {
    "id": 2,
    "title": "درباره",
    "link": "/about",
    "megaMenu": False,
    "subMenu": False
  },
  {
    "id": 3,
    "title": "خدمات",
    "link": "/services",
    "megaMenu": False,
    "subMenu": False
  },
  {
    "id": 4,
    "title": "تیم",
    "link": "/team",
    "megaMenu": False,
    "subMenu": False
  },
  {
    "id": 5,
    "title": "وبلاگ",
    "link": "/blog-grid-right-sidebar",
    "megaMenu": False,
    "subMenu": [
      {
        "title": "وبلاگ شبکه ای با ستون راست",
        "link": "/blog-grid-left-sidebar"
      },
      {
        "title": "وبلاگ شبکه ای با ستون چپ",
        "link": "/blog-grid-right-sidebar"
      },
      {
        "title": "وبلاگ شبکه ای بدون ستون",
        "link": "/blog-grid-without-sidebar"
      },
      {
        "title": "وبلاگ فهرستی با ستون راست",
        "link": "/blog-list-left-sidebar"
      },
      {
        "title": "وبلاگ فهرستی با ستون چپ",
        "link": "/blog-list-right-sidebar"
      },
      {
        "title": "جزئیات وبلاگ",
        "link": "/blog/wild-life-workshop?id=14"
      }
    ]
  },
  {
    "id": 6,
    "title": "تماس",
    "link": "/contact"
  }
]
    return HttpResponse(json.dumps(data), content_type='application/json')


@api_view(['''GET'''])
def pricing_table_data(request):
    return HttpResponse(json.dumps(pricing_table()), content_type='application/json')


@api_view(['''GET'''])
def services_data(request):
    return HttpResponse(json.dumps(services()), content_type='application/json')


@api_view(['''GET'''])
def sidebar_data(request):
    return HttpResponse(json.dumps(sidebar()), content_type='application/json')


@api_view(['''GET'''])
def slider_data(request):
    return HttpResponse(json.dumps(slider()), content_type='application/json')


@api_view(['''GET'''])
def social_networks_data(request):
    return HttpResponse(json.dumps(social_networks()), content_type='''application/json''')


@api_view(['''GET'''])
def team_data(request):
    return HttpResponse(json.dumps(team()), content_type='''application/json''')


@api_view(['''GET'''])
def testimonial_data(request):
    return HttpResponse(json.dumps(testimonials()), content_type='''application/json''')
