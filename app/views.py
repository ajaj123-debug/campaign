from django.shortcuts import render, redirect
from .models import FundraisingCampaign
from django.http import HttpResponse
from django import forms

# Create your views here.

class FundraisingCampaignForm(forms.ModelForm):
    class Meta:
        model = FundraisingCampaign
        fields = ['title', 'description', 'goal_amount', 'image']


def home(request):
    # Retrieve all campaigns from the database
    campaigns = FundraisingCampaign.objects.all()
    
    return render(request, 'home.html', {'campaigns': campaigns})


def create_campaign(request): 
    # Handle the creation of a fundraising campaign
    if request.method == 'POST':
        form = FundraisingCampaignForm(request.POST, request.FILES)

        if form.is_valid():
            # Log the form data and errors for debugging
            print("Form cleaned data:", form.cleaned_data)
            print("Form errors:", form.errors)

            # Save the campaign instance and redirect to the detail page
            campaign = form.save()  # Let the form handle saving the image as well
            return redirect('campaign_detail', id=campaign.id)  # Redirect to the detail page of the created campaign

        else:
            print("Form is invalid")
            print("Form errors:", form.errors)
            # If the form is invalid, show the form with errors
            return render(request, 'create_campaign.html', {'form': form})

    else:
        form = FundraisingCampaignForm()

    return render(request, 'create_campaign.html', {'form': form})


def campaign_detail(request, id): 
    # Display the details of a specific campaign
    campaign = FundraisingCampaign.objects.get(id=id)
    return render(request, 'campaign_detail.html', {'campaign': campaign})

from decimal import Decimal

def donate(request):
    campaigns = FundraisingCampaign.objects.all()  # Retrieve all campaigns for the dropdown

    # Handle the donation process
    if request.method == 'POST':
        amount = Decimal(request.POST.get('amount'))  # Convert the amount to a Decimal
        campaign_id = request.POST.get('campaign')  # Get the campaign ID from the form
        
        # Retrieve the selected campaign
        campaign = FundraisingCampaign.objects.get(id=campaign_id)
        
        # Update the current amount of the campaign
        campaign.current_amount += amount  # Now this will work since both are Decimal
        
        campaign.save()  # Save the updated campaign

        return redirect('home')  # Redirect to the home page or a success page

    upi_number = "your-upi-number@example.com"  # Replace with actual UPI number
    instructions = "Please open your payment app and pay the amount to the UPI number above."
    return render(request, 'donate.html', {
        'campaigns': campaigns,
        'upi_number': upi_number,
        'instructions': instructions
    })
