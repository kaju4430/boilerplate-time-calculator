def add_time(start, duration, day=None):
    
    new_time = dict()
    start_time = dict()
    added_time = dict()
    days_to_add = None
    hours_to_add = None
    minutes_added = None
    am_pm = ""
    
    start_time["hour"] = int(start.split()[0].split(":")[0])
    start_time["minutes"] = int(start.split()[0].split(":")[1])

    added_time["hour"] = int(duration.split(":")[0])    
    added_time["minutes"] = int(duration.split(":")[1])
    
    am_pm = start.split()[1]

    days_to_add = int(added_time["hour"] / 24)
    hours_to_add = added_time["hour"] % 24
    minutes_added = int(start_time["minutes"] + added_time["minutes"])

    if minutes_added >= 60:
        minutes_added -= 60
        hours_to_add += 1

    new_time["hour"] = start_time["hour"] + hours_to_add
    if new_time["hour"] >= 12:
        new_time["hour"] -= 12
        if am_pm == "PM":
            am_pm = "AM"
            days_to_add += 1
        
        else:
            am_pm = "PM"

    new_time["minutes"] = minutes_added

    new_time["ampm"] = am_pm

    new_time["days"] = "("+str(days_to_add)+" days later)"

    #for k, v in start_time.items():
        #print(k, v)

    #for k, v in added_time.items():
        #print(k, v)

    for k, v in new_time.items():
        print(k, v)


    quit()
    return new_time