from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import logout

class ProfileCompletionMiddleware:
    """Profile completion middleware.

    Ensure every user that is interacting with the platform
    have their profile picture and biography.
    """

    def __init__(self, get_response):
        """Middleware initialization."""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view is called."""
        print(request)
        if not request.user.is_anonymous:
            try:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('users:update_profile'), reverse('users:logout')]:
                        return redirect('users:update_profile')
            except:
                logout(request)
                return render(request, 'login.html', {'error': 'User has no profile'})

        response = self.get_response(request)
        return response
