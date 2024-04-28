from django.shortcuts import render, redirect
from .models import Review, Contact_Us
from .forms import AddReviewForm, AddContactForm

# Create your views here.
def home_view(request):
    return render(request, 'main/index.html')


def about_view(request):
    return render(request, 'main/about.html')

def product_view(request):
    return render(request, 'main/product.html')

def contact_view(request):
    forms=AddContactForm()
    if request.method=='post':
        forms=AddContactForm(request.POST)
        if forms.is_valid:
            forms.save()
            return redirect ('home')
    context={
            'forms':forms
        }
    return render(request, 'main/contact.html', context) 


def testimonial_view(request):
    return render(request, 'main/testimonial.html')


def add_review(request):
    forms=AddReviewForm()
    if request.method=='POST':
        forms=AddReviewForm(request.POST)
        if forms.is_valid():
            post=forms.save(commit=False)
            post.name=request.user
            post.save()
            return redirect('home')
        
    context={
        'forms':forms,
        'message': 'your review has been successfully submitted'
    }
    return render (request, 'main/add_review.html', context)
