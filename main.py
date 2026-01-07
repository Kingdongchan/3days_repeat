#입력
idx = int(input())

#처리
members = [
    {"name": "김동찬", "age": 27},
    {"name": "공욱재", "age": 26}   
]

def is_valid_index(members, idx):
    if idx >= 0 and idx < len(members):
        return True
    return False

#출력
if is_valid_index(members, idx):
    print(members[idx])
else:
    print("잘못된 인덱스")