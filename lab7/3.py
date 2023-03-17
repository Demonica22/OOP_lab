input_file = input("Enter input file name:\n")
output_file = input("Enter output file name: \n")

try:
    with open(input_file, 'r', encoding='utf-8') as input_file:
        buffer = input_file.read()
    with open(output_file, 'w', encoding='utf-8') as output_file:
        output_file.write(buffer.upper())
    print("File done normally")
except FileNotFoundError:
    print("File doesn't exist")
except Exception:
    print("Some error found")