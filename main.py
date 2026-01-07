#입력
keyword = input()

#처리
members = [
    {"name": "김동찬", "age": 27},
    {"name": "공욱재", "age": 26}
]

def read_by_name(members, keyword):
    for member in members:
        if member["name"] == keyword:
            return member
    return None

#출력
result = read_by_name(members, keyword)
print(result)
