class BungeoBbang:
    def __init__(self, contents, price):
        self.contents = contents
        self.price = price
        self.total_sales = 0

    def sell(self):
        print(f"{self.contents} 붕어빵을 {self.price}원에 판매했습니다.")
        self.total_sales += self.price

    def eat(self):
        print(f"{self.contents} 붕어빵을 먹었습니다.")

    def display_total_sales(self):
        print(f"총 판매금: {self.total_sales}원")

# "슈크림 붕어빵" 객체 생성
cream_bungeo = BungeoBbang("슈크림", 1500)

# "팥 붕어빵" 객체 생성
red_bean_bungeo = BungeoBbang("팥", 1200)

# "슈크림 붕어빵" 판매 및 먹기
cream_bungeo.sell()
cream_bungeo.eat()
cream_bungeo.display_total_sales()

# "팥 붕어빵" 판매 및 먹기
red_bean_bungeo.sell()
red_bean_bungeo.eat()
red_bean_bungeo.display_total_sales()
