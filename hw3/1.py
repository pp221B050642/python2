with open("students.txt", "r") as stu:
    stu2 = open("students2.txt", "w")
    all = stu.read().split("\n")
    for student in all:
        info = student.split()
        info[0] = info[0].capitalize()
        info[1] = info[1].capitalize()
        info[3] = "301-"+info[3]
        stu2.write(f"{info[0]} {info[1]} {info[2]} {info[3]}\n")
