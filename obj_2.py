class cat:

    #color는 클래스 멤버(변수)
    color = 'red'

    #생성자 메소드  --클래스의 시작 주소
    def __init__(self, name, color):
        self.name = name
        self.color = color

    #인스턴스 메소드의 변수는 일반적으로 self로 약속
    def meow(self):
        print("우리 {}이는 색깔이 {}이고요. 자주 야옹~ 야옹~! 거려요.".format(self.name, self.color))

raon = cat('라온', "똥")
meon = cat('미용', '컬러풀하')
raon.meow()
print(meon.color)
meon.meow()