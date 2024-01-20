"""This Python script demonstrates a simple yet effective way to find the highest score from a list of student scores without relying on built-in functions 
like max. The code employs a straightforward algorithm that iterates through the list using a for loop, 
comparing each score with the current highest score found so far. """
# Sample Input = 150 142 185 120 171 184 149 199
# Expected Output = 199

# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
highscr = 0
for score in student_scores:
  if score > highscr:
    highscr = score
    

print(f"The highest score in the class is: {highscr}")
