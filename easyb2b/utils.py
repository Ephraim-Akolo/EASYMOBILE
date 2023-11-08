from datetime import datetime
import random

_alphnum = [chr(i) for i in range(48, 58)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]

def get_easyb2b_reference(code_len=16) -> str:
    date = datetime.now().strftime("%Y%m%d%I%M")
    code = ''.join(random.sample(_alphnum, code_len))
    return f"{date}{code}"

