from multiprocessing.connection import answer_challenge
import random
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = {
    "What's one effect of calling random.seed(42)": [
        "The random numbers are reproducible.",
        "The random numbers are more random.",
        "The computer clock is reset.",
        "The first random number is always 42.",
    ],
    "When does __name__ == '__main__' equal True in a Python file": [
        "When the file is run as a script",
        "When the file is imported as a module",
        "When the file has a valid name",
        "When the file only has one function",
    ]
}

def prepare_questions(questions,num_questions):
  num_questions = min(num_questions, len(questions))
  return random.sample(list(questions.items()), k = num_questions)

def get_answer(question, alternatives):
  print(f"{question}?")
  labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
  for label, alternative in labeled_alternatives.items():
    print(f"{label} {alternative}")
  while (answer_label := input ("\nChoice?")) not in labeled_alternatives:
    print(f"Please answer one of {','.join(labeled_alternatives)}")
    
  return labeled_alternatives[answer_label]
  
def ask_question(question, alternatives):
  correct_answer = alternatives[0]
  ordered_alternatives = random.sample(alternatives, k=len(alternatives))