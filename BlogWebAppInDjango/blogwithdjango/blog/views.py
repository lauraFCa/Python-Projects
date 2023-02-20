from django.shortcuts import render

# A view is a place where we put the "logic" of our application. 
# It will request information from the model you created before and pass it to a template

def post_list(request):
    return render(request, 'blog/post_list.html', {})