from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from Code import extract_text_from_image, extract_text_from_pdf

def process_image(request):
    if request.method == 'POST' and request.FILES['image']:
        # Save the uploaded image
        image_file = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        uploaded_image_path = fs.path(filename)
        
        # Process the image to extract text
        extracted_text = extract_text_from_image(uploaded_image_path)
        
        # Render the result template with the extracted text
        return render(request, 'home.html', {'text': extracted_text})

    
    return render(request, 'home.html')

def process_pdf(request):
     if request.method == 'POST' and request.FILES['pdf']:
        # Save the uploaded image
        image_file = request.FILES['pdf']
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        uploaded_image_path = fs.path(filename)
        # Process the image to extract text
        extracted_text = extract_text_from_pdf(uploaded_image_path)
        
        
        # Render the result template with the extracted text
        return render(request, 'pdf.html', {'text': extracted_text})

     return render(request,'pdf.html')

def homw(request):
    return render(request,'Choice.html')


