def add_time(start, duration, day=None):
    
    new_time = ""
    start_time = dict()
    added_time = dict()
    days_to_add = None
    am_pm = ""
    
    start_time["hour"] = int(start.split()[0].split(":")[0])
    start_time["minutes"] = int(start.split()[0].split(":")[1])

    added_time["hour"] = int(duration.split(":")[0])    
    added_time["minutes"] = int(duration.split(":")[1])
    
    am_pm = start.split()[1]

    #days_to_add = 
    
        
    
    for k, v in start_time.items():
        print(k, v)

    for k, v in added_time.items():
        print(k, v)

    print(am_pm)
    quit()
    return new_time