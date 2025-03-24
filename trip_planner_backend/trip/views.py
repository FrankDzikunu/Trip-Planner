from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime, timedelta

@api_view(['POST'])
def generate_log_sheet(request):
    """
    Generate log sheets based on trip details.
    """
    data = request.data
    current_location = data.get('currentLocation')
    pickup_location = data.get('pickupLocation')
    dropoff_location = data.get('dropoffLocation')
    cycle_used = int(data.get('cycleUsed', 0))

    if not all([current_location, pickup_location, dropoff_location]):
        return Response({'error': 'All fields are required'}, status=400)

    logs = []
    start_time = datetime.now().replace(hour=8, minute=0, second=0)  # Start at 8 AM

    logs.append({"time": start_time.strftime('%I:%M %p'), "activity": "Start Trip", "location": current_location})
    start_time += timedelta(hours=4)  # After 4 hours, stop for fuel

    logs.append({"time": start_time.strftime('%I:%M %p'), "activity": "Fuel Stop", "location": "Fuel Station"})
    start_time += timedelta(hours=3)  # After 3 hours, stop for rest

    logs.append({"time": start_time.strftime('%I:%M %p'), "activity": "Rest Break", "location": "Rest Area"})
    start_time += timedelta(hours=3)  # After another 3 hours, trip ends

    logs.append({"time": start_time.strftime('%I:%M %p'), "activity": "End Trip", "location": dropoff_location})

    return Response({"logs": logs}, status=200)
