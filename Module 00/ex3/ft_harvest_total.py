def ft_harvest_total() -> None :
    first_day = int(input("Day 1 harvest: "))
    second_day = int(input("Day 2 harvest: "))
    third_day = int(input("Day 3 harvest: "))
    if first_day < 0 or second_day < 0 or third_day < 0 :
        print("Harvest amounts must be positive numbers.")
    else :
        print("Total harvest: ", first_day + second_day + third_day)
