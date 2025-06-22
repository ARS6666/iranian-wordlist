def generate_birthyears(name, start_year=1950, end_year=2026, output_file="name_birthMyears.txt"):
    with open(output_file, "w", encoding="utf-8") as f:
        for year in range(start_year,end_year):
            f.write(f"{name}{year}\n")
    print(f"Birthdate combinations written to '{output_file}'.")

name_input = input("Enter a name: ")
generate_birthyears(name_input.strip())


        