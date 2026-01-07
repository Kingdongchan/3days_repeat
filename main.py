#입력
menu = input()

#처리
members = [
    {"name": "김동찬", "age": 27}
]

def read_all(members):
    for member in members:
        print(member)
        
def get_count(members):
    return len(members)

#출력
if menu == "1":
    read_all(members)
elif menu == "2":
    print(get_count(members))