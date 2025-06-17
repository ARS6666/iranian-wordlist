#Change this list so it suits your needs
valid_numbers = {
    "0912": {342, 541, 241, 242, 642, 772, 878, 542, 141, 841},  
    "0910": {484, 472, 971, 446, 475, 483, 479, 639},
    "0991": {591, 119, 115, 207},
    "0990": {991, 847, 912, 446, 419},
    "0919": {821, 339, 338, 335, 336, 274}
}

def generate_iranian_numbers():
    numbers = []  
    for prefix in valid_numbers:
        for yyy in valid_numbers[prefix]:
            for zzzz in range(0, 10000): 
                formatted_zzzz = f"{zzzz:04d}" 
                numbers.append(f"{prefix}{yyy}{formatted_zzzz}")  
    return numbers

file_name = "iranian_numbers.txt"
numbers = generate_iranian_numbers()

with open(file_name, "w") as file:
    for number in numbers:
        file.write(number + "\n")

print(f"Generated {len(numbers)} numbers and saved them to {file_name}")
