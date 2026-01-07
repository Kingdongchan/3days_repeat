#입력
def show_menu():
    print("1. 조회")
    print("2. 종료")
    
def read_all(members):
    for member in members:
        print(member)
        
#처리
def main():
    members = [
        {"name": "김동찬", "age": 27}
    ]
    while True:
        show_menu()
        menu = input()
        if menu == "1":
            read_all(members)
        elif menu == "2":
            break
#출력
main()
