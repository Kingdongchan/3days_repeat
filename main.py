#입력
target_name = input()
new_age = int(input())

#처리
members = [
    {"name": "김동찬", "age": 27},
    {"name": "공욱재", "age": 26}
]

def update_by_name(members, target_name, new_age):
    for member in members:
        if member["name"] == target_name:
            member["age"] = new_age

#출력
update_by_name(members, target_name, new_age)
print(members)
