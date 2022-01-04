def swappingFile():

    file1 = input("Enter the file1 path: ")
    file2 = input("Enter the file2 path: ")

    with open(file1, "r") as a:
        data_a = a.read()
        print("From file1: ",data_a)

    with open(file2, "r") as b:
        data_b = b.read()
        print("From file2: ",data_b)

    print("After Swaping file")

    with open(file2, "w") as b:
        b.write(data_a)
        print("From file1: ",data_b)

    with open(file1, "w") as a:
        a.write(data_b)
        print("From file2: ",data_a)

swappingFile()