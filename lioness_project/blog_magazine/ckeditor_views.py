import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.files.storage import default_storage


@csrf_exempt
@require_POST
def custom_upload_file(request):
    if "upload" not in request.FILES:
        return JsonResponse({"error": {"message": "No file provided"}}, status=400)

    f = request.FILES["upload"]
    try:
        name = default_storage.save(f.name, f)
        url = default_storage.url(name)
        return JsonResponse({"url": url})
    except Exception as e:
        return JsonResponse({"error": {"message": str(e)}}, status=500)
