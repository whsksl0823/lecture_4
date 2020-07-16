class cat:
    #color는 클래스 멤버(변수)
    color = 'red'              
    #인스턴스 메소드의 변수는 일반적으로 self로 약속
    def meow(self):             
        print("야옹~ 야옹~!")

#raon 객체, cat 객체
raon = cat()
nabi = cat()
tong = cat()

raon.meow()
nabi.meow()
tong.meow()