from django.db import connection
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def health_check(request):
    try:
        connection.ensure_connection()

        return Response({
            "status": "ok",
            "database": "connected"
        })

    except Exception:
        return Response({
            "status": "error",
            "database": "disconnected"
        }, status=500)