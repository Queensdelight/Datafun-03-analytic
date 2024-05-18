''' This module provides a reusable byline for the author's services. '''

#import independencies
import pathlib
import time
import bukola_utils

def create_folders_for_range(start, end):
    """
    Create folders for a given range (e.g., years).
    """
    for i in range(start, end + 1):
        pathlib.Path(f"{i}").mkdir(exist_ok=True)

def create_folders_from_list(folder_list):
    """
    Create folders from a list of names.
    """
    for folder in folder_list:
        pathlib.Path(folder).mkdir(exist_ok=True)

def create_prefixed_folders(folder_list, prefix):
    """
    Create prefixed folders by transforming a list of names and combining each with a prefix.
    """
    for folder in folder_list:
        pathlib.Path(f"{prefix}-{folder}").mkdir(exist_ok=True)

def create_folders_periodically(duration):
    """
    Create folders periodically (e.g., one folder every 5 seconds).
    """
    start_time = time.time()
    while(time.time()-start_time < duration): #continue running while the time elapsed from start is less than the given duration
        current_time = time.time()-start_time
        pathlib.Path(f"Folder created at {round(current_time)} seconds").mkdir(exist_ok=True)
        time.sleep(duration) #wait specified amount of seconds before beginning next iteration


import pathlib
# Create a path object
project_path = pathlib.Path.cwd()

# Define the new sub folder path
data_path = project_path.joinpath('data')

# Create new if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)



def main():
    ''' Main function to demonstrate module capabilities. '''

    # Print byline from imported module
    print(f"Byline:{bukola_utils.byline}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2024)

    # Call function 2 to create folders given a list
    folder_names = ['South', 'North', 'East']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['length', 'height', 'width']
    prefix = 'measurement-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs = 10  # duration in seconds
    create_folders_periodically(duration_secs)

    # Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g. function 2) 
    # Call your function and test these options
    regions = [
      "Nebraska", 
      "Illinois", 
      "Kansas", 
      "South Dakota", 
      "Iowa", 
      "Michigan", 
      "Alabama"
    ]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)


if __name__ == '__main__':
    main()