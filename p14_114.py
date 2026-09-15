import string

MAPPING = string.digits + string.ascii_uppercase

source, source_type, target_type = tuple(input().split(" "))

source_type, target_type = int(source_type), int(target_type)

number = int(source, source_type)

if number == 0:
    print(0)
    exit()

target = list()
while number > 0:
    number, remainder = divmod(number, target_type)
    target.append(MAPPING[remainder])

print("".join(target)[::-1])