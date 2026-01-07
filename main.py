#입력

#처리
def create_person(name, age):
    return {"name": name, "age": age}

def show_pserson(person):
    print(person["name"], person["age"])
    
#출력
person = create_person("김동찬", 27)
show_pserson(person)