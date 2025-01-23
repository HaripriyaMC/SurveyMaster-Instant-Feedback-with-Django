from django.shortcuts import render , redirect
from .models import *

def index(request):
    feedbacks = CustomerFeedback.objects.all()
    return render(request, 'surveys.html',{'feedbacks':feedbacks})
    
def customer_feedback(request, id):
    feedback = CustomerFeedback.objects.get(id=id)
    if request.method == 'POST':
        for question in feedback.question.all():
            response_text = request.POST.get(f"response_{question.id}")
            selected_options_ids = request.POST.getlist(f"option_{question.id}")

            print(f"Creating response for question {question.id}")
            print(f"Response Text: {response_text}")
            print(f"Selected Option IDs: {selected_options_ids}")

            response = CustomerResponse.objects.create(
                feedback=feedback,
                question=question,
                response_text=response_text if question.question_type in ["Text", "BigText"] else None
            )
            
            if selected_options_ids:
                selected_options = Options.objects.filter(id__in=selected_options_ids)
                response.selected_options.set(selected_options)
        
        return redirect('/thank-you/')
    return render(request, 'survey.html', {'questions': feedback.question.all()})

def thank_you(request):
        return render(request, "thank_you.html")