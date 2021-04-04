from datetime import datetime
import datetime

def get_current_year_to_context(request):
    current_datetime = datetime.datetime.now()
    
    now=current_datetime
    current_time = now.strftime("%H:%M:%S")
    return{
        'current_time': current_time
       }