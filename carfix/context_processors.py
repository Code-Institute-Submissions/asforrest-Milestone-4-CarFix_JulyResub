from profiles.models import UserProfile


def total_credits(request):
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        total_credits = profile.total_credits
        return {"total_credits" : total_credits}
    else:
        return {"total_credits" : "No"}
