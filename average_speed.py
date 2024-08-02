def average_speed():
    time = minutes_to_hour + seconds_to_hour
    distance = 14 / one_mile
    speed = distance / time
    return f"The average speed is {speed:.2f} miles per hour."



seconds = 30
seconds_to_hour = seconds / (60 * 60)
minutes = 45
minutes_to_hour = minutes / 60
one_mile = 1.6
print(average_speed())