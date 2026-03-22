
print("Welcome to a fun facts Quiz Game! 🎰")
print("Let's begin.")

questions = ("In which country was Elon Musk born?: ",
             "What year did World War II end?: ",
             "How many bones are in the human body?: ",
             "Which animal sleeps standing up and can't vomit?: ",
             "What creature has three hearts and blue blood?: ")

options = (("A. South Africa", "B. Japan ", "C. Dakota", "D. Los Angeles"), # first question
           ("A. 1941", "B. 1942", "C. 1940 ", "D. 1945 "), # second question
           ("A. 206", "B. 207 ", "C. 208 ", "D. 209 "),
           ("A. Koalas", "B. White Polar Bear ", "C. Horses", "D. Spiders "),
           ("A. Seahorse", "B. Octopus", "C. Hippopotamus", "D. Seagull "))

answers = ("A", "D", "A", "C", "B")
guesses = []      # appending guesses to our list, which is why I'm using a list rather than a tuple.
score = 0
question_number = 0

for question in questions:
    print("---------------------")
    print(question)
    for option in options[question_number]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("Correct! ")
    else:
        print("Incorrect!")
        print(f"{answers[question_number]} is the correct answer. ")
    question_number += 1


print("---------------------")
print("       RESULTS 🧮    ")
print("---------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")