#입력
target_name = input()

#처리
members = [
    {"name": "김동찬", "age": 27},
    {"name": "공욱재", "age": 26},
    {"name": "정승훈", "age": 25}
]

def delete_by_name (members, target_name):
    for i, member in enumerate(members):
        if member["name"] == target_name:
            members.pop(i)
            break

#출력
delete_by_name(members, target_name)
print(members)
