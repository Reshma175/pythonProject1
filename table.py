# Print user input table
def table5(limit):
    for i in range(1, limit + 1):
        result = 5 * i
        print(f"5 x {i} = {result}")


user_input = int(input("Enter the limit for the table of 5: "))
table5(user_input)