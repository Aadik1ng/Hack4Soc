
def basic_feature(income, avg_expenses, goal, time):
    """Basic feature calculation.

    Args:
        income (float): Monthly income.
        avg_expenses (float): Average monthly expenses.
        goal (float): Desired savings goal.
        time (float): Desired time to reach goal.

    Returns:
        float: Basic feature calculation.
    """

    if (goal / time > income - avg_expenses):
        print("You are not saving enough to reach your goal in the given time.")
        can_save = int(input("How much can you save per month? "))
        return can_save

    else:
        print(f"You need to save {goal / time} per month to reach your goal in the given time.")



income = int(input("What is your monthly income? "))
avg_expenses = int(input("What is your average monthly expenses? "))
goal = int(input("What is your desired savings goal? "))
time = int(input("In how many months do you want to reach your goal? "))
can_save = basic_feature(income, avg_expenses, goal, time)