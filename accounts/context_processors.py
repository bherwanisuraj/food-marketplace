from .models import UserProfile

def get_profile(request):
    try:
        userprofile = UserProfile.objects.get(user=request.user)
        
    except:
        userprofile = None
    
    return dict(userprofile=userprofile)