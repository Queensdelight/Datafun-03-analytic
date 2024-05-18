"""My Python Utils"""

import math
import statistics

my_name: str = "Denise Case"
course_count: int = 6
is_experienced: bool = True
hours_invested: float = 2.5
numbers: list = [7, 6, 5, 8, 8, 4, 5, 7, 8, 6]

my_name_string = f"Author: {my_name}"
course_count_string: str = f"{course_count=}"
is_experienced_string: str = f"{is_experienced=}"
hours_invested_string: str = f"{hours_invested=}"
numbers_string: str = f"{numbers=}"

radius: float = 6.0
area: float = math.pi * radius**2
radius_area_string: str = f"Math: Given {radius=}, {area=}"

# stats
count: int = len(numbers)
smallest: int = min(numbers)  # not min  - that's a built in function
largest: int = max(numbers)  # not max  - that's a built in function
mode: float = statistics.mode(numbers)
median: float = statistics.median(numbers)
mean: float = statistics.mean(numbers)
stdev: float = round(statistics.stdev(numbers),2)

my_stats_string: str = f"""
Recent Daily Water Counts
-------------------------
{count=}
{smallest=}
{largest=}
{mode=}
{median=}
{mean=}
{stdev=}
"""

def main():
    ''' Display all the output'''
    print(my_name_string)
    print(course_count_string)
    print(is_experienced_string)
    print(hours_invested_string)
    print(numbers_string)
    print(radius_area_string)
    print(my_stats_string)

# only call main() and display output if this script is executed directly
if __name__ == "__main__":
    main()  # Run the module main() function
