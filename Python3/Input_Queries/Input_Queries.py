# Program to ask the user a question and give a reply based on input recieved

user_input = input("Do you want to hear a joke?")

if ((user_input == "yes") | (user_input == "Yes") | (user_input == "Y") | (user_input == "y")):
    user_input = input("Why do blind people hate skydiving?")
    print("Because it scares the shit out of their dogs!")
else:
    print("Oh ok ):")