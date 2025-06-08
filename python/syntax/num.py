# range = range(1,100)

# for num in range:
#     if num == 98:
#         print("Found it!")
#         continue
#     print(num)

# daily_reminder.py

# Step 1: Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 2: Process the task with a match-case block (Python 3.10+)
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority"

# Step 3: Modify message based on time sensitivity
if time_bound == "yes":
    message += " that requires immediate attention today!"

# Step 4: Output the customized reminder
print("\nReminder:", message)
