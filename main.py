#입력
def show_menu():
    print("1. 추가")
    print("2. 전체조회")
    print("3. 수정")
    print("4. 삭제")
    print("5. 종료")
    
def add_member(members):
    name = input()
    age = int(input())
    members.append({"name": name, "age": age})
    
def read_all(members):
    for idx, member in enumerate(members):
        print(idx, member["name"], member["age"])
        
def update_member(members):
    idx = int(input())
    new_age = int(input())
    members[idx]["age"] = new_age
    
def delete_member(members):
    idx = int(input())
    members.pop(idx)
    
#처리
def main():
    members = []
    while True:
        show_menu()
        menu = input()
        if menu == "1":
            add_member(members)
        elif menu == "2":
            read_all(members)
        elif menu == "3":
            update_member(members)
        elif menu == "4":
            delete_member(members)
        elif menu == "5":
            break
        
#출력
main()