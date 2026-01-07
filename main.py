#입력
idx = int(input())

#처리
member = [
    {"name": "김동찬", "age": 27},
    {"name": "공욱재", "age": 26}
]

def read_by_index(member, idx):
    return member[idx]

#출력
result = read_by_index(member, idx)
print(result)
