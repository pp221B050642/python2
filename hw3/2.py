with open("first file.txt", "r") as file1:
    with open("second file.txt", "r") as file2:
        file3 = open("third file.txt", "w")
        lines1 = file1.read().split("\n")
        lines2 = file2.read().split("\n")
        for i in range(len(lines1)):
            k = lines1[i]+lines2[i]
            file3.write(str(k)+"\n")
