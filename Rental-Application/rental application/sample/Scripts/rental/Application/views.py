from django.shortcuts import get_object_or_404, redirect,render
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import register_form,login_form,PropertyForm,PropertyUpdateForm
from .models import Profile,Property,Like,PropertyImage
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import PropertyForm, PropertyImageFormSet
from django.db import transaction
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings




def register(request):
    if request.method == 'POST':
        form = register_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            else:
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    email=form.cleaned_data['Email'],
                    password=form.cleaned_data['password']
                )
                Profile.objects.create(
                    user=user,
                    phone_number=form.cleaned_data['phone_no']
                )
                messages.success(request, 'Registration successful. Please log in.')
                return redirect('login')
    else:
        form = register_form()
    return render(request, 'register.html', {'form': form})



def login_f(request):
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                messages.error(request, "Invalid Password or Username")
                return redirect('/login/')

    else:
        form = login_form()
    return render(request, 'login.html', {'form': form})

def main(request):
    if request.method == 'POST':
        filter_param = request.POST.get('filter_param', '')
        filter_value = request.POST.get('filter_value', '')
        properties = Property.objects.all()
        filter_kwargs = {}
        if filter_param and filter_value:
            if filter_param in ['place', 'area', 'nearby_landmark', 'property_type']:
                filter_kwargs = {f'{filter_param}__icontains': filter_value}
            elif filter_param in ['bedrooms', 'bathrooms']:
                try:
                    filter_kwargs = {filter_param: int(filter_value)}
                except ValueError:
                    filter_kwargs = {}
        
        properties = properties.filter(**filter_kwargs)
    else:
        
        properties = Property.objects.all()

    p = Paginator(properties,3)
    page_number = request.GET.get('page')
    final_data = p.get_page(page_number)
    total_page = final_data.paginator.num_pages
    total_list = [n+1 for n in range(total_page)]
    user_likes = Like.objects.filter(user=request.user).values_list('property_id', flat=True) if request.user.is_authenticated else []
    context = {
        'properties': final_data,
        'user_likes': user_likes,
        'total_pages':total_page,
        'total_list':total_list
    }
    return render(request, 'main.html', context)

    
    


@login_required
def like_property(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    user = request.user
    liked = Like.objects.filter(user=user, property=property).exists()
    if request.method == 'POST':
        page_number = request.POST.get('page')
    if not liked:
        Like.objects.create(user=user, property=property)
        property.likes += 1
    else:
        Like.objects.filter(user=user, property=property).delete()
        property.likes -= 1

    property.save()
   
    # Construct the redirect URL with the current page number
    

    return redirect(f'/main/?page={page_number}')
    
    
def create_property(request):
    if request.method == 'POST':
        property_form = PropertyForm(request.POST)
        image_formset = PropertyImageFormSet(request.POST, request.FILES, queryset=PropertyImage.objects.none())

        if property_form.is_valid() and image_formset.is_valid():
            with transaction.atomic():
                property_instance = property_form.save(commit=False)
                property_instance.user = request.user
                property_instance.save()

                for form in image_formset.cleaned_data:
                    if form:
                        image_instance = form['image']
                        PropertyImage.objects.create(property=property_instance, image=image_instance)
                
                return redirect('main') 
    else:
        property_form = PropertyForm()
        image_formset = PropertyImageFormSet(queryset=PropertyImage.objects.none())

    return render(request, 'post_property.html', {
        'property_form': property_form,
        'image_formset': image_formset,
    })


@login_required
def history(request):
    properties = Property.objects.filter(user=request.user)
    return render(request, 'history.html', {'properties': properties})

def property_update(request,property_id):
    return render(request,'history.html')

def property_delete(request,property_id):
    property = get_object_or_404(Property, id=property_id, user=request.user)
    property.delete()
    return redirect(reverse('history'))


@login_required
def property_update(request, property_id):
    property = get_object_or_404(Property, id=property_id, user=request.user)
    if request.method == 'POST':
        form = PropertyUpdateForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return redirect('history')
    else:
        form = PropertyUpdateForm(instance=property)
    return render(request, 'update.html', {'form': form})



@login_required
def property_images(request, property_id):
    property = get_object_or_404(Property, id=property_id, user=request.user)
    if request.method == 'POST':
        formset = PropertyImageFormSet(request.POST, request.FILES, queryset=PropertyImage.objects.filter(property=property))
        if formset.is_valid():
            formset.instance = property
            formset.save()
            return redirect('property_images', property_id=property.id)
    else:
        formset = PropertyImageFormSet(queryset=PropertyImage.objects.filter(property=property))
    return render(request, 'property_images.html', {'property': property, 'formset': formset})


@login_required
def delete_image(request, image_id):
    image = get_object_or_404(PropertyImage, id=image_id, property__user=request.user)
    property_id = image.property.id
    image.delete()
    return redirect('property_images', property_id=property_id)


def interested(request,property_id):
    property = get_object_or_404(Property, id=property_id)
    images = PropertyImage.objects.filter(property=property)
    profile = Profile.objects.get(user=property.user)

   
    seller_subject = 'Someone is interested in your property'
    seller_message = f'The customer details:\n\nName: {request.user.first_name} {request.user.last_name}\nEmail: {request.user.email}\n'
    seller_email = property.user.email

    
    customer_subject = 'Seller details for your interested property'
    customer_message = f'The seller details:\n\nName: {property.user.first_name} {property.user.last_name}\nEmail: {property.user.email}\n'
    customer_email = request.user.email

    
    send_mail(
        seller_subject,
        seller_message,
        settings.EMAIL_HOST_USER,
        [seller_email],
        fail_silently=False,
    )

    # Send email to the customer
    send_mail(
        customer_subject,
        customer_message,
        settings.EMAIL_HOST_USER,
        [customer_email],
        fail_silently=False,
    )

    # Prepare context for the template
    context = {
        'property': property,
        'seller': property.user,
        'phone_no':profile.phone_number,
        'images': images
    }

    return render(request, 'interested.html', context)

