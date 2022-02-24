# Problem_code - SQUIDRULE
test_cases = int(input("Enter number of test cases: "))
for num in range(test_cases):
    players = int(input("Enter number of players: "))
    money_add = input("Enter the amount of money to be added: ")
    money_add = money_add.split(" ")
    money_add1 = list(map(lambda x:int(x),money_add))
    money_add1.remove(min(money_add1))
    print(sum(money_add1))