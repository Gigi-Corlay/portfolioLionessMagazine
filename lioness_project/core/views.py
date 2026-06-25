from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def legal_notice(request):
    return render(request, "legals_notices/legal_notice.html")


def privacy_policy(request):
    return render(request, "legals_notices/privacy_policy.html")


def terms_of_use(request):
    return render(request, "legals_notices/terms_of_use.html")


def cookie_policy(request):
    return render(request, "legals_notices/cookie_policy.html")
