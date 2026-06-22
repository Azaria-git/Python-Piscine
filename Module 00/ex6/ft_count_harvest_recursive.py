def helper_function(days, current_day = 1) -> int :
    if current_day > days :
        print("Harvest time!")
    else :
        print("Day ", current_day)
        helper_function(days, current_day + 1)

def ft_count_harvest_recursive() -> None :
    days = int(input("Days until harvest: "))
    if days <= 0 :
        print("Days until harvest must be more than 0.")
    else :
        helper_function(days)
