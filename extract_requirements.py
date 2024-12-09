def read_file(file_path):
    """
    Reads the content of a text file.

    Args:
        file_path (str): The path to the text file.

    Returns:
        str: The content of the file as a string.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: The file at '{file_path}' was not found."
    except IOError as e:
        return f"Error reading file: {e}"


file_path = 'data/regulation.txt'  
file_content = read_file(file_path)
print(file_content)
