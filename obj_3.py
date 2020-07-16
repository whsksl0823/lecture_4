class cat:

    #color는 클래스 멤버(변수)
    color = 'red'

    #생성자 메소드  --클래스의 시작 주소
    def __init__(self, name, color):
        self.name = name
        self.color = color

    #인스턴스 메소드의 변수는 일반적으로 self로 약속
    def meow(self, name):
        print('우리 고양이는 못생긴 {}'.format(name))
        print("길냥이 {}이는 색깔이 {}고요. 자주 야옹~ 야옹~! 거려요.".format(self.name, self.color))

# gang_cat = cat('미옹', '컬러풀하')
# jong_cat = cat('태경', '똥이')
# gang_cat.meow('라온')
# jong_cat.meow('라온')