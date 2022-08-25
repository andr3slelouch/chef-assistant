import os.path


def get_working_directory() -> str:
    """
    Allows to get the working directory for the project
    :return: Full path to the working directory
    """
    user_dir = os.path.expanduser("~")
    working_directory = os.path.join(user_dir, "ChefAssistant")
    if not os.path.exists(working_directory):
        os.makedirs(working_directory)
    return working_directory


def get_file_from_working_directory(file_name: str) -> str:
    """
    Generates a full path to a file from the working directory

    :param: file_name: Filename to be got from the working directory
    :return: Full path to the file in the working directory
    """
    return os.path.join(get_working_directory(), file_name)
