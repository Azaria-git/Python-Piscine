def ft_count_harvest_iterative() -> None :
    days = int(input("Days until harvest: "))
    if days <= 0 :
        print("Days until harvest must be more than 0.")
        return
    for i in range(1, days + 1) :
        print("Day ", i)
    print("Harvest time!")