from datetime import datetime
import random

# Define the alphanumeric characters
_alphnum = [chr(i) for i in range(48, 58)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]

def get_easyb2b_reference(code_len: int = 16) -> str:
    """
    Generate a unique reference code for a transaction by combining the current date-time string and a random alphanumeric code.
    Args:
        code_len (int, optional): The length of the random alphanumeric code. Default is 16.
        
    Returns:
        str: The generated reference code.
    """
    date_str = datetime.now().strftime("%Y%m%d%I%M")
    random_code = ''.join(random.sample(_alphnum, code_len))    
    return f"{date_str}{random_code}"


