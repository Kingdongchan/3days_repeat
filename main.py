#입력
def get_person_input():
    name = input()
    age = int(input())
    return {"name": name, "age": age}

#처리

#출력
person = get_person_input()
print(person)

