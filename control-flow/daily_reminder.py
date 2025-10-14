task = input("Enter your Task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it Time-bound? (yes/no): ")


match priority:
    case 'high':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print("this is a high no priority")
    case 'medium':
        if time_bound == 'yes':
            print("this is a medium priority")
        else:
            print("this is a medium no priority")
    case 'low':
        if time_bound == 'yes':
            print("this is a low priority")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("This is a default")

   

  