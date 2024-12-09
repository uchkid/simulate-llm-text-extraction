import json
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

def split_text_into_paragraphs(content):
    """
    Splits the given text into paragraphs.

    Args:
        content (str): The input text.

    Returns:
        list: List of paragraphs.
    """
    
    paragraphs = content.strip().split('\n\n')
    
    paragraphs = [paragraph.strip() for paragraph in paragraphs]
    return paragraphs

def simulate_llm_summary(paragraph):
    """
    Summarizes paragraph by extracting the portion of text from the beginning up to the second period.
    This logic returns first sentence

    Args:
        paragraph (str): The input text.

    Returns:
        str: The summarized text.
    """  
    
    # Split the text by periods
    split_by_period = paragraph.split('.')

    # Check if there are at least two periods
    if len(split_by_period) > 2:
        paragraph_summary = '.'.join(split_by_period[:2]) + '.'
    else:
        # If there are fewer than two periods, return the entire paragraph
        paragraph_summary = paragraph 

    return paragraph_summary

def save_to_json(file_path, json_output):
    """
    Saves an item to a JSON file.

    Args:
        file_path (str): The path to the JSON file.
        json_output (dict): The item to save, represented as a dictionary.
    """
    
    # Save to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(json_output, file, indent=4)

def summarize_llm():
    file_path = 'data/regulations.txt'
    content = read_file(file_path)
    paragraphs = split_text_into_paragraphs(content)
    json_output = []

    for i, paragraph in enumerate(paragraphs, 1):
        summary_text =  simulate_llm_summary(paragraph)
        summary_data = {
            "Section number": i,
            "Original text":paragraph,
            "Summarized requirements":summary_text,
            "Source": "https://www.gov.uk/government/publications/ai-regulation-a-pro-innovation-approach/white-paper"
        }
        json_output.append(summary_data) 

    output_file_path = 'data/regulations_output_summary.json' 
    save_to_json(output_file_path, json_output)

if __name__ == "__main__":
    summarize_llm()
