
#//Do not import any Python libraries.
def add_time(start:str, duration:str, weekday:str="")->str:
    week = ["monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday"]
    is_pm = True
    start, midday = start.split(' ')
    start = [int(x) for x in start.split(":")]
    duration = [int(x) for x in duration.split(":")]
    if midday == "AM":
        is_pm = not is_pm
    
    time = []
    time.append(start[0] + duration[0])
    time.append(start[1] + duration[1])
    time[0] += time[1] // 60
    time[1] = time[1] % 60
    
    past_half_day = time[0] // 12
    day_count = past_half_day // 2
    if is_pm and past_half_day % 2 == 1:
        day_count += 1
    if past_half_day % 2 == 1:
        is_pm = not is_pm
    time[0] = time[0] % 12
    if not time[0]:
        time[0] = 12
    
    result = f"{time[0]}:{time[1]:02d} {'PM' if is_pm else 'AM'}"
    
    if weekday:
        result += f", {week[(week.index(weekday.lower())+day_count) % 7].capitalize()}"
    if day_count:
        if day_count == 1:
            result += f" (next day)"
        else:
            result += f" ({day_count} days later)"
    return result

if __name__=="__main__":
    print(add_time("3:00 PM", "3:10"))
    print("Returns: 6:10 PM\n")

    print(add_time("11:30 AM", "2:32", "Monday"))
    print("Returns: 2:02 PM, Monday\n")

    print(add_time("11:43 AM", "00:20"))
    print("Returns: 12:03 PM\n")

    print(add_time("10:10 PM", "3:30"))
    print("Returns: 1:40 AM (next day)\n")

    print(add_time("11:43 PM", "24:20", "tueSday"))
    print("Returns: 12:03 AM, Thursday (2 days later)\n")

    print(add_time("6:30 PM", "205:12"))
    print("Returns: 7:42 AM (9 days later)\n")