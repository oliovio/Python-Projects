print("Welcome to my quiz game!")

playing = input("Do you want to play?  ")
print(playing)
if playing.lower() != "yes":
    print("Okay! Goodbye!")
    quit()
print("Okay! Let's play :)")
answer = input("What does CPU stand for?  ")
if answer == "central processing unit":
    print("Correct!")
else: answer != "central processing unit"
print("Incorrect!")