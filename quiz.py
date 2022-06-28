from asyncore import write
import enum
from webbrowser import get


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
for question, alternatives in QUESTIONS2.items():
  correct_answer = alternatives[0]
  sorted_alternatives = sorted(alternatives)
  for label, alternative in enumerate(sorted_alternatives):
    print(f" {label} {alternative}")
  answer_label = int(input(f"{question}?"))
  answer = sorted_alternatives[answer_label]
  if answer == correct_answer:
    print ("Correct!")
  else:
    print(f"the answer is {correct_answer!r} not {answer!r}")
