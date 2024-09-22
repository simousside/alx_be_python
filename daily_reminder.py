# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority using match-case
match priority:
    case 'high':
        reminder = f"'{task}' is a high priority task."
    case 'medium':
        reminder = f"'{task}' is a medium priority task."
    case 'low':
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = "Invalid priority. Please enter high, medium, or low."

# Check if the task is time-sensitive and modify the reminder accordingly
if time_bound == 'yes':
    reminder += " It requires immediate attention today!"
elif time_bound == 'no':
    reminder += " Consider completing it when you have free time."

# Output the reminder
print("\nReminder:", reminder)
