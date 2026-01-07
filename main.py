#입력
idx = int(input())
new_age = input()

#처리
members = [
    {"name": "김동찬", "age": 27},
    {"name": "공욱재", "age": 26}
]

def update_by_index(members, idx, new_age):
    members[idx]["age"] = new_age

#출력
update_by_index(members, idx, new_age)
print(members)
