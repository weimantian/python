numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # 输出: [1, 2, 5, 5, 6, 9] # 基本排序示例

students = [('Alice', 25, 'A'), ('Bob', 20, 'B'), ('Charlie', 20, 'A')]

# 首先按年龄排序，然后按成绩排序 # 双重排序示例
sorted_students = sorted(students, key=lambda x: (x[1], x[2]))
print(sorted_students)  # 输出: [('Bob', 20, 'B'), ('Charlie', 20, 'A'), ('Alice', 25, 'A')]

numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers_desc = sorted(numbers, reverse=True)
print(sorted_numbers_desc)  # 输出: [9, 6, 5, 5, 2, 1] # 逆序排序示例

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self):
        return f"Student(name={self.name}, age={self.age}, grade={self.grade})"

students = [
    Student('Alice', 25, 'A'),
    Student('Bob', 20, 'B'),
    Student('Charlie', 20, 'A')
]

# 使用key参数按年龄排序 # 自定义类排序示例
sorted_students_by_age = sorted(students, key=lambda s: s.age)
print(sorted_students_by_age)  # 输出: [Student(name=Bob, age=20, grade=B), Student(name=Charlie, age=20, grade=A), Student(name=Alice, age=25, grade=A)]