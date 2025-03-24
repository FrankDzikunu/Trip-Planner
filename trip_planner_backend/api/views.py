from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def generate_trip(request):
    data = request.data
    trip_details = {
        "current_location": data.get("current_location"),
        "pickup_location": data.get("pickup_location"),
        "dropoff_location": data.get("dropoff_location"),
        "current_cycle": data.get("current_cycle"),
        "message": "Trip route generated successfully!"
    }
    return Response(trip_details)
