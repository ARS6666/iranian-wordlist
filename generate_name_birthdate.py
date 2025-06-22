def is_valid_date(day, month, year):
    if month < 1 or month > 12 or day < 1:
        return False
    if month <= 6:
        return day <= 31
    elif month <= 11:
        return day <= 30
    else:
        return day <= 29

def generate_birthdates(name, start_year=1350, end_year=1404, output_file="name_birthdates.txt"):
    with open(output_file, "w", encoding="utf-8") as f:
        for year in range(start_year, end_year + 1):
            for month in range(1, 13):
                for day in range(1, 32):
                    if is_valid_date(day, month, year):
                        date_str = f"{year}{month:02d}{day:02d}" 
                        f.write(f"{name}{date_str}\n")
    print(f"Birthdate combinations written to '{output_file}'.")

name_input = input("Enter a name: ")
generate_birthdates(name_input.strip())
