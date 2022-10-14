import mysql.connector as mysql
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Fairy.tale01",
    database = "test")

cursor = db.cursor()

def get_prof_detail(prof_id):
    id = f"select Prof_id from professor where Prof_id = {prof_id}"
    name = f"select Prof_name from professor where Prof_id = {prof_id}"
    uni_id = f"select Uni_id from professor where Prof_id = {prof_id}"
    jdate = f"select Joining_date from professor where Prof_id = {prof_id}"
    speciality = f"select Speciality from professor where Prof_id = {prof_id}"
    salary = f"select Salary from professor where Prof_id = {prof_id}"
    exp = f"select Experience from professor where Prof_id = {prof_id}"
    
    cursor.execute(id)
    i = cursor.fetchall()
    print(f"Professor id:", end = " ")
    print(*i[0])

    cursor.execute(name)
    n = cursor.fetchall()
    print(f"Professor name:", end = " ")
    print(*n[0])
    
    cursor.execute(uni_id)
    u = cursor.fetchall()
    print(f"University id:", end = " ")
    print(*u[0])

    cursor.execute(jdate)
    j = cursor.fetchall()
    print(f"Joining date:", end = " ")
    print(*j[0])

    cursor.execute(speciality)
    s = cursor.fetchall()
    print(f"Speciality:", end = " ")
    print(*s[0])

    cursor.execute(salary)
    sa = cursor.fetchall()
    print(f"Salary:", end = " ")
    print(*sa[0])

    cursor.execute(exp)
    e = cursor.fetchall()
    print(f"Experience:", end = " ")
    print(*e[0])

def get_spec_prof_list(speciality, salary):
    profes = f"select Prof_id from professor where Speciality = '{speciality}' and Salary >= {salary}"
    cursor.execute(profes)
    professors = cursor.fetchall()
    for i in professors:
        for j in i:
            get_prof_detail(j)
            print()

get_spec_prof_list("Math", 2000)