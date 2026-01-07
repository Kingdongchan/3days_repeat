#입력
idx = int(input())

#처리
members = [
    {"name": "김동찬", "age": 27},
    {"name": "공욱재", "age": 26},
    {"name": "정승훈", "age": 25}
]

def delete_by_index(members, idx):
    members.pop(idx)
    
#출력
delete_by_index(members, idx)
print(members)
