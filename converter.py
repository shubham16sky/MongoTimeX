from datetime import datetime,timezone
import pytz

def objidToTime(obj_id):

    if len(obj_id) != 24:
        raise ValueError("Input must be a 24-character long string")


    hex_time_stamp = obj_id[:8]
    epoch_time_stamp = int(hex_time_stamp,16)

    #convert to iso format in UTC 
    datetime_object_utc = datetime.fromtimestamp(epoch_time_stamp, tz=timezone.utc)
    #utc_iso_time = datetime_object_utc.isoformat()
    utc_iso_time = datetime_object_utc.strftime("%Y-%m-%dT%H:%M:%S%z")

    #convert to iso format in IST
    ist_timezone = pytz.timezone('Asia/Kolkata')
    datetime_object_ist = datetime_object_utc.astimezone(ist_timezone)
    ist_iso_time = datetime_object_ist.strftime("%Y-%m-%dT%H:%M:%S%z")

    return utc_iso_time,ist_iso_time


def timeToId(year,month,date,hour,minute,second):

    if year is None and month is None and date is None and hour is None and minute is None and second is None:
        raise ValueError("Values can't be empty")
            


    year=str(year)
    month = str(month)
    date = str(date)
    hour = str(hour)
    minute = str(minute)
    second = str(second)

    
    
    
    dateAndTime = year+"-"+month+"-"+date+"T"+hour+":"+minute+":"+second+"+0000"
    parsed_datetime = datetime.strptime(dateAndTime, "%Y-%m-%dT%H:%M:%S%z")
    epoch_timestamp = parsed_datetime.timestamp()
    hex_value = hex(int(epoch_timestamp))+"0000000000000000"
    return hex_value[2:]




    


    



