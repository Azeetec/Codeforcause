from django.urls import path
from project import views
from accounts.decorators import *
urlpatterns = [

    path('', NonProfitRequired(views.ProjectListing.as_view()), name = 'ProjectListing'),
    path('view_project/', NonProfitRequired(views.ProjectView.as_view()), name = 'ProjectView'),
    path('developer_project/',DeveloperRequired(views.DeveloperProjectListing.as_view()), name = 'DeveloperProjectListing'),
    path('AddProject/',NonProfitRequired(views.AddProject.as_view()), name = 'AddProject'),

    path('profile/',views.ProfileView.as_view(), name = 'ProfileView'),
    path('developer_profile/',views.DeveloperProfileView.as_view(), name = 'DeveloperProfileView'),
    path('DeveloperListing/',views.DeveloperListing.as_view(), name = 'DeveloperListing'),
    path('deliver/',views.DeliverOrder.as_view(), name = 'DeliverOrder'),

    path('assigned/',NonProfitRequired(views.AssignedProject.as_view()), name = 'AssignedProject'),
    path('bid/',DeveloperRequired(views.ProjectBid.as_view()), name = 'ProjectBid'),
    path('chat/',NonProfitRequired(views.ChatPage.as_view()), name = 'ChatPage'),
    path('chat1/',DeveloperRequired(views.ChatPage1.as_view()), name = 'ChatPage1'),
    path('home/',views.HomePage.as_view(), name = 'HomePage'),
    path('about/',views.AboutPage.as_view(), name = 'AboutPage'),

    path('ReviewDelivery/',views.ReviewDelivery.as_view(), name = 'ReviewDelivery'),
    path('ApproveOrNot/',views.ApproveOrNot.as_view(), name = 'ApproveOrNot'),
    path('Cancelled/',views.Cancelled.as_view(), name = 'Cancelled'),


]