patterns = [123456789,12345678,1234567,123456,12345,12234,123,12,1,21,321,4321,54321,654321,7654321,87654321,987654321,1234567890987654321,'.','..','...',"!",'!!','!!!',"@",'@@','@@@',"#",'##','###','$','$$','$$$','&','&&','&&&','*','**','***','****','*****','******','*******','********']
def generate_patterns(name , output_file="name_patterns.txt"):
    with open(output_file, "w", encoding="utf-8") as f:
        for pattern in patterns:
            f.write(f"{name}{pattern}\n")
            f.write(f"{pattern}{name}\n")
    print(f"Birthdate combinations written to '{output_file}'.")

name_input = input("Enter a name: ")
generate_patterns(name_input.strip())


        