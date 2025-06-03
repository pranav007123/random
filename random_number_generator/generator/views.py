from django.shortcuts import render
import random

def home(request):
    random_number = None
    excluded_numbers = []
    
    if request.method == 'POST':
        # Get excluded numbers from the form
        excluded_input = request.POST.get('excluded_numbers', '')
        if excluded_input:
            try:
                excluded_numbers = [int(x.strip()) for x in excluded_input.split(',') if x.strip()]
            except ValueError:
                excluded_numbers = []
        
        # Generate random number excluding the specified numbers
        available_numbers = [x for x in range(1, 61) if x not in excluded_numbers]
        if available_numbers:
            random_number = random.choice(available_numbers)
    
    return render(request, 'generator/home.html', {
        'random_number': random_number,
        'excluded_numbers': ','.join(map(str, excluded_numbers))
    })
