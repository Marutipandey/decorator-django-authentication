from django.shortcuts import redirect
from functools import wraps

def login_required_custom(view_func):
   
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # If the user is a superuser, they bypass the login check
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)

        if not request.user.is_authenticated:
            return redirect('login')  
        
        # If the user is authenticated but not a superuser, continue
        return view_func(request, *args, **kwargs)
    
    return _wrapped_view
