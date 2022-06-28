name = input("what's your name?")

print(name)

answer = input("when was the first known use of the word 'quiz'?")
if answer == "1781":
  print("Correct!")
else:
  print(f"the answer is '1781', not {answer!r}")