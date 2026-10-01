s = input()

is_negative = s.startswith("-")
if is_negative or s.startswith("+"):
    body = s[1:]
else:
    body = s

rev_body = body[::-1]

if "." in rev_body:
    int_part, dec_part = rev_body.split(".", 1)
    
    int_part = int_part.lstrip("0")
    if int_part == "":
        int_part = "0"
        
    dec_part = dec_part.rstrip("0")
    
    if dec_part == "":
        formatted_body = int_part
    else:
        formatted_body = f"{int_part}.{dec_part}"
else:
    int_part = rev_body.lstrip("0")
    if int_part == "":
        int_part = "0"
    formatted_body = int_part

result = f"-{formatted_body}" if is_negative else formatted_body
print(result)