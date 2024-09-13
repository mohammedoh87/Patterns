print("Right-Angled Triangle Pattern")
num_rows = int(input("Enter the number of rows: "))

for i in range(num_rows):
    for j in range(i + 1):
        print("* ", end = "")
    print()    

    