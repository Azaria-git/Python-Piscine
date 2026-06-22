def ft_water_reminder() -> None :
    last_watering = int(input("Days since last watering: "))
    if last_watering < 0 :
        print("Days since last watering must be a positive number.")
    elif last_watering > 2 :
        print("Water the plants!")
    else :
        print("Plants are fine.")
