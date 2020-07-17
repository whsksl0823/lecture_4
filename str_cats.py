class Cat :
    def __init__(self, name, color):
        self.name = name
        self.color = color

    #호출을 하지 않아도 class의 자체 메소드로 문자열을 반환한다.
    def __str__(self):
        # print('Cat(name='+self.name+', color='+self.color+')')
        return 'Cat(name='+self.name+', color='+self.color+')'

nabi = Cat('나비', '검정색') 
nero = Cat('네로', '흰색')
print(nabi)
print(nero)