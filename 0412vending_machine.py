# 개발 전 시나리오 작성
# 0. 판매 음료 보여주기
# 1. 사용자가 음료를 입력
# 2. 음료에 따른 가격 입력
# 3. 사용자가 금액 투입
# 4. 재고가 부족하지 않으면 음료 반환 후 재고 1개 삭제
# 5. 잔돈 반환

vending_machine = {
    'drinks': ['사이다','콜라', '생수'],
    'price': [1300, 1500, 900],
    'stock': [4, 2, 1]
}

money = 0 # 사용자가 넣을 돈

while True:
    buyable_count = 0 # 구매 가능한 음료 개수

    print("-------판매하고 있는 음료-------") # stock 이 1개 이상이면 판매 가능
    for i in range(3):
        if vending_machine['stock'][i] > 0:
            print(f'{vending_machine['drinks'][i]}-{vending_machine['price'][i]}원')


    money += int(input("자판기에 금액을 투입해주세요: "))
    print(f"투입 금액은 {money}입니다.")
    

    # 구매 가능한 음료 선택
    print("-------구매할 음료 선택-------")
    for i in range(3):
        if money >= vending_machine['price'][i] and vending_machine['stock'][i] > 0:
            print(f'{vending_machine['drinks'][i]}-{vending_machine['price'][i]}원')
            buyable_count += 1
    if money < 900 or buyable_count == 0:
        print("구매할 수 있는 음료가 없습니다.")
    elif buyable_count > 1 and money >= 900:
        choice_drink = input("구매할 음료를 선택해주세요: ")
        if choice_drink in vending_machine['drinks']:
            idx = vending_machine['drinks'].index(choice_drink)
            vending_machine['stock'][idx] -= 1
            money -= vending_machine['price'][idx]
            print(f'{choice_drink} 1개가 나왔습니다. 반환구를 확인해주세요.')
        if money > 0:
            print(f"잔돈은 {money}원입니다.")
        else:
            print('반환할 돈이 없습니다.')
    exit = input("종료하시겠습니까? y|n : ")
    if exit == 'y':
        break
if money > 0:
    print(f"잔돈 {money}원을 반환합니다. 이용해주셔서 감사합니다.")