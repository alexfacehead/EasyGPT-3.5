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

def replace_question(user_input_q):
    template = AUTOMATED_CONTEXT_CALLER
    
    return template.replace("[Question]", user_input_q)