# Print the sum of the current number and the previous number


current_num = 0
for i in range (1,11):
    current_num = i
    previous_num = i -1

    print(f"current number is {current_num} and previous number is {previous_num} Sum is {current_num+previous_num}")
