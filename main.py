#입력

#처리
members = [
    {"name": "김동찬", "age": 27},
    {"name": "공욱재", "age": 26}
]

def read_all_with_index(index):
    for idx, member in enumerate(members):
        print(idx, member["name"], member["age"])
        
#출력
read_all_with_index(members)