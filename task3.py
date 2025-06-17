import re

def normalize_phone(phone_number):
    digits = re.sub(r"[^\d+]", "", phone_number.strip())
    if digits.startswith("+"):
        return "+" + re.sub(r"[^\d]", "", digits)
    elif digits.startswith("380"):
        return "+" + re.sub(r"[^\d]", "", digits)
    elif digits.startswith("0"):
        return "+38" + re.sub(r"[^\d]", "", digits)
    else:
        return "+38" + re.sub(r"[^\d]", "", digits)
    
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]   
print(sanitized_numbers)