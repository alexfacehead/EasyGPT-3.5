from src.utils.constants import AUTOMATED_CONTEXT_CALLER

def sum_content_length(messages):
    """
    Function to sum up the length of the content values in a list of messages.
    
    Args:
        messages (list of dict): List of message dictionaries.
    
    Returns:
        int: The total length of all content strings.
    """
    total_length = 0
    for message in messages:
        content = message.get('content', '')
        total_length += len(content)
        
    return total_length

def format_string(s: str) -> str:
    """Format a string to show the first 7 characters, last 4 characters, with stars in between.

    Args:
        s (str): The input string

    Returns:
        str: The formatted string

    Raises:
        ValueError: If the length of the string is 0
    """
    
    if len(s) == 0:
        raise ValueError("The input string must not be empty.")
    
    return s[:7] + '*' * 7 + s[-4:]