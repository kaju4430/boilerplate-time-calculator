def add_time(start, duration, day=None):
    
    new_time = dict()
    result_time = ""
    start_time = dict()
    added_time = dict()
    days_to_add = None
    hours_to_add = None
    minutes_added = None
    am_pm = ""
    days_of_the_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    
    start_time["hour"] = int(start.split()[0].split(":")[0])
    start_time["minutes"] = int(start.split()[0].split(":")[1])

    #time to be added
    added_time["hour"] = int(duration.split(":")[0])    
    added_time["minutes"] = int(duration.split(":")[1])
    
    am_pm = start.split()[1]

    #whole number of days minus the extra hours (fractional part)
    days_to_add = int(added_time["hour"] / 24)
    #remaining hours
    hours_to_add = added_time["hour"] % 24

    minutes_added = int(start_time["minutes"] + added_time["minutes"])

    if minutes_added >= 60:
        #increment hour
        minutes_added -= 60
        hours_to_add += 1

    #add each component to new_time dict
    new_time["hour"] = start_time["hour"] + hours_to_add

    #change PM to AM or vice versa if the hours to be added is greater than or equal to 12
    if new_time["hour"] >= 12:
        #12 hours format is required, so the hour loops back to 1 and the am_pm flag is flipped
        #midnight hour is to be shown as 12 and not 00, so loop back by subtracting 12 is skipped if hours added is exactly 12
        if new_time["hour"] != 12:
            new_time["hour"] -= 12
        if am_pm == "PM":
            am_pm = "AM"
            #increment days to be added if PM flips to AM after adding the hours
            days_to_add += 1
        
        else:
            am_pm = "PM"

    #formatting minutes component to have 2 digits
    new_time["minutes"] = str(minutes_added).rjust(2, '0')

    new_time["ampm"] = am_pm

    result_time += str(new_time["hour"]) + ":" + str(new_time["minutes"]) + " " + new_time["ampm"]

    if day:
        day = day.lower()
        tmp = days_to_add % 7
        #index of day passed as argument
        pos = days_of_the_week.index(day)
        pos += tmp

        #loop back after end of week
        if pos == 7:
            pos = 0
 
        new_time["day"] = days_of_the_week[pos].capitalize()

        result_time += ", " + new_time["day"]

    if days_to_add > 1:
        new_time["day_length"] = "("+str(days_to_add)+" days later)"

        result_time += " " + new_time["day_length"]

    elif days_to_add == 1:
        new_time["day_length"] = "(next day)"

        result_time += " " + new_time["day_length"]

    print(result_time)
    #quit()

    return result_time