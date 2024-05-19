import pandas as pd
import sympy as sp
from sympy import symbols , pi 
questions = []
choices = [] 

pi = sp.pi
r = symbols('r')
d = symbols('d') 
question1 = 'Area of the Circle if radius of the circle is  4 and value of pi is assumed as 3.14 is  \n A) 12.56 \n B) 200.96 \n C) 50.24 \n D) 25.12'
choice1 = 'C' 
question2 = 'The No.of Intersections Points of two parallel lines is \n A) 0 \n B) 1 \n C) 2  \n D) None of the above'
choice2 = 'A' 
question3 = '''The Number of Ways of arranging the string "LOVE" with or without meaning is given by \n A) 4 \n B) 6 \n C) 12 \n D) 24'''
choice3 = 'D'
question4 = '''Arjun is the son of the daughter of shanti , Shanti is the wife of son of Ramireddy . Then the relation of shanti with Ramireddy is   \n A) Daughter \n B) Daughter in Law \n C) Sister \n D) Son in Law
  '''
choice4 = 'B'
question5 = 'What is the Limiting Values of the expression sin(x)/x as x tends to 0 and infinity \n A) 0 , 1 \n B) 1 , 0 \n C) 0 , 0 \n D)1 , 1'
choice5 = 'B'
question6 = 'can you tell me the output of the python code snippet \n\t print(eval("3"+"3")) \n A) "6" \n B) "33" \n C) 6 \n D) 33 '
choice6 = 'D'
question7 = 'What is the average of the series 2 , 4 , 8 , 16 ..... upto 10 terms  \n A) 2046 \n B) 1022  \n C) 510 \n D) 4094 '
choice7 = 'A'
question8 = 'No.of Diogonals of a Polygon of 7 sides is \n A)21 \n B)15 \n C)14 \n D)None of the Above '
choice8 = 'C'
question9 = 'The sum of the squares of the numbers 1,2,3,4,5 ,.... upto 30 is given by \n A) 465 \n B) 310 \n C) 7440 \n D) 4960 '
choice9 = 'D'
question10 = 'The value of the follwing expression is given by 2+8*3-9/3+4-7*2 if * denotes the multiplication operator \n A) 8 \n B) 13 \n C) 5.34 \n D) 17' 
choice10 = 'B'

print(question1)
print(question2)
print(question3)
print(question4)
print(question5)
print(question6)
print(question7)
print(question8)
print(question9)
print(question10)

questions.append(question1)
choices.append(choice1)
questions.append(question2)
choices.append(choice2)
questions.append(question3)
choices.append(choice3)
questions.append(question4)
choices.append(choice4)
questions.append(question5)
choices.append(choice5)
questions.append(question6)
choices.append(choice6)
questions.append(question7)
choices.append(choice7)
questions.append(question8)
choices.append(choice8)
questions.append(question9)
choices.append(choice9)
questions.append(question10)
choices.append(choice10)




question_answer = {'questions' : questions , 'choices' : choices}
QuizQuestions = pd.DataFrame(question_answer)

QuizQuestions.to_csv('QuizQuestions.csv')