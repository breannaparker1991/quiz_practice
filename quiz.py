from string import ascii_lowercase


name = input("what's your name?")

print(name)

answer = input("when was the first known use of the word 'quiz'?")
if answer == "1781":
  print("Correct!")
else:
  print(f"the answer is '1781', not {answer!r}")
  
QUESTIONS = [
  ("What is my dog's name?", "Snickers"), 
  ("Which keyword do you use to loop over a give list of elements?", "for")
]

for question, correct_answer in QUESTIONS:
  answer = input(f"{question}?")
  if answer == correct_answer:
    print("Correct!")
  else:
    print(f"The answer is {correct_answer!r}, not {answer!r}")
    
QUESTIONS2 = {
  "What's the purpose of the built-in zip() function": [
        "To iterate over two or more sequences at the same time",
        "To combine several strings into one",
        "To compress several files into one archive",
        "To get information from the user",
    ],
    "What's the name of Python's sorting algorithm": [
        "Timsort", "Quicksort", "Merge sort", "Bubble sort"
    ],
}
num_correct = 0
for num, (question, alternatives) in enumerate (QUESTIONS2.items(), start =1):
  print(f"\nQuestion {num}:")
  print(f"{question}?")
  correct_answer = alternatives[0]
  labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
  for label, alternative in labeled_alternatives.items():
    print(f" {label} {alternative}")
  while (answer_label := input("\nChoice?")) not in labeled_alternatives:
    print(f"Please answer one of {',' .join(labeled_alternatives)}")

  answer = labeled_alternatives[answer_label]
  if answer == correct_answer:
    num_correct += 1
    print ("⭐Correct!⭐")
  else:
    print(f"the answer is {correct_answer!r} not {answer!r}")

print(f"\nYou got {num_correct} correct out of {num} questions")
