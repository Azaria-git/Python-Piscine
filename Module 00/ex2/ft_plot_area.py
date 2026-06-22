def ft_plot_area() -> None :
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    if length < 0 or width < 0 :
        print("Length and width must be positive numbers.")
    else :
        print("Plot area: ", length * width)
 