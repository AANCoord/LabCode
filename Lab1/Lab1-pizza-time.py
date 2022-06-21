# Author: Adam Valencia

from math import ceil, pi

def main():
    
    print('Welcome to Joe\'s Pizza Converter. Est. 2022!')
    diameter_standard = int(input("What is the diameter of a \"standard\" size pie? "))
    radius = diameter_standard / 2

    standard_slices = int(input("How many slices are in a standard size pie? "))

    needed_slices = int(input("How many standard slices do you want? "))

    super_diameter = int(input("What is the diameter of the pies you will buy? "))
    super_radius = super_diameter / 2

    # Give us the area of the pizza per slice
    standard_area = pi * (radius ** 2);
    standard_slice_area = standard_area / standard_slices;

    # Gives us the amount of pizza we need in total
    standard_pizza_needed = standard_slice_area * needed_slices;

    # Gives us the area of the super pies
    super_pie_area = pi * (super_radius ** 2);

    # Calculate the amount of super pies needed
    super_pies_needed =  standard_pizza_needed / super_pie_area;

    super_pies = ceil(super_pies_needed);
    

    print()
    # print("You will need to buy " + str(super_pies) + " " + str(super_diameter) + "-inch diameter pies.")
    print(f"You will need to buy {super_pies} {super_diameter}-inch diameter pies.")
    


    # print(radius)
    # print(standard_slices)
    # print(needed_slices)
    # print(super_radius)
    # Print()

if __name__ == "__main__":
    main()




