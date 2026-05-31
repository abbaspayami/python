def budget_manager(initial_budget):
    total_budget = initial_budget

    def my_budget(action, amount = 0):
        nonlocal total_budget
        if action == 'add':
            total_budget = total_budget + amount
            print(f"income : {amount}. current budget: {total_budget}")
        elif action == 'spend':
            if amount > total_budget:
                print(f"Budget is not enough, amount is {amount}، but current budget is {total_budget}")
            else:
                total_budget -= amount
                print(f"spend : {amount}. current budget: {total_budget}")
        elif action == "get":
            print(f"current budget : {total_budget}")
            return total_budget
        else:
            print("invalid operation!")

    return my_budget

my_budget = budget_manager(1000)
my_budget('add', 500)
my_budget('spend', 300)
my_budget('get')
my_budget('spend', 1500)