#입력

#처리
def get_name():
    return "김동찬"

def get_greeting():
    name = get_name()
    return name + "님 안녕하세요"

#출력
message = get_greeting()
print(message)