ifo_str = """"
********************
欢迎使用学生寝室管理系统
请选择你要进行的操作
1.新建学生信息
2.显示全部信息
3.查询学生信息
4.删除学生信息
5.修改学生信息
0.退出系统
*******************              
 """

students = [
    {
        'name':'小王',
        'sno':'11',
        'sex':'男',
        'bed':'100'
    }
]

while True:
    print(ifo_str)
    action = input("请输入想要的操作")
    if action =='0':
        print("退出系统")
        break
    elif action == '1':
        print("新建学生信息")
        name = input("请输入名字: ")
        sno = input("请输入学号: ")
        sex = input("请输入性别: ")
        bed = input("请输入寝室: ")
        student = {
            'name': name,
            'sno': sno,
            'sex': sex,
            'bed': bed
        }
        students.append(student)

    elif action == '2':
        print("显示学生信息")
        for student in students:
            print(student)
    elif action == '3':
        print("查询学生信息")
        name = input("请输入需要查询的学生名字: ")
        for student in students:
            if student['name'] == name:
                print(student)
        else:
            print(f"{name} 学生信息不存在")

    elif action == '4':
        print("删除学生信息")
        name = input('请输入要删除的学生名字：')
        for student in students:
            if student['name'] == name:
                students.remove(student)
                break
        else:
            print(f"{name} 学生信息不存在")

    elif action == '5':

        print("修改学生信息")
        name = input("请输入修改学生的名字: ")
        for student in students:
            if student['name'] == name:
                student['name'] = input("请输入名字: ")
                student['sno'] = input("请输入学号: ")
                student['sex'] = input("请输入性别: ")
                student['bed'] = input("请输入寝室: ")
        else:
            print(f"{name} 学生信息不存在")

    else:
        print("你输入的错误，请重新输入")






