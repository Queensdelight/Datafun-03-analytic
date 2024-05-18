'''Start a data analytics project.'''

import pathlib


def create_project_directory(directory_name):
    """
    Creates a project sub-directory.
    :param directory_name: Name of the directory to be created, e.g. "test"
    """
    pathlib.Path(directory_name).mkdir(exist_ok=True)

def create_project_directory(directory_name: str) -> None:


    def main():
        ''' Scaffold a project. '''
        create_project_directory(directory_name='test') # I named the parameter
        create_project_directory(directory_name='docs') # I named the parameter



    
    if __name__ == '__main__':
        main()