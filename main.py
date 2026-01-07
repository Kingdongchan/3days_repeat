#입력
min_age = int(input())

#처리
members = [
    {"name": "김동찬", "age": 27},
    {"name": "공욱재", "age": 26},
    {"name": "정승훈", "age": 25}
]

def search_by_age(members, min_age):
    result = []
    for member in members:
        if member["age"]==min_age:
            result.append(member)
            
#출력
filtered = search_by_age(members, min_age)
print(members)
