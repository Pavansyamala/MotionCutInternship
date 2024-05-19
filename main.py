import pandas as pd
import threading

class QuizGame:
    def __init__(self):
        self.score = 0 
        self.unattempted = 0 
        self.wronganswers = 0 
        self.totalQuestions = 10
        self.questions_answers = pd.read_csv('QuizQuestions.csv') 
        self.questions = self.questions_answers.questions 
        self.answers = self.questions_answers.choices
        print()
        print('\n\t************** Welcome to the Quiz on Basic Mathematics and Aptitude 2024 *******************\t\n ')
        self.username = input(' Enter Your Full Name : ')
        self.user = input("\n Enter y in order to proceed to the  quiz else n  [y/n] : ")
        if self.user == 'y' or self.user == 'Y': 
            self.Instructions()

    def Instructions(self):
        instructions = '''\n Instructions for your Quiz is as follows : \n
         1. Total Number of Questions in the Quiz are 10 \n 
         2. Each Question Carries 1 Mark \n 
         3. Time for Each Question is 1.5 minutes \n 
         4. Minimum Score to clear the test is 6 marks\n
         5. Each Question carries 4 Multiple Choices in which only 1 option is the correct choice\n'''
        print(instructions)
        understood = input("Enter y for to proceed to quiz else n  [y/n] : ")
        if understood == 'y' or understood == 'Y':
            self.StartQuiz()
    
    def StartQuiz(self):

        while self.totalQuestions > 0 :

            self.totalQuestions -= 1 
            question = self.questions[self.totalQuestions]
            correct_choice = self.answers[self.totalQuestions]
            print(question)
            def getAnswer():
                answer = input("Enter your Answer : ")
                answer = answer.strip()
                if answer == correct_choice or ord(answer)-ord(correct_choice)== 32 :
                    self.score += 1
                    print('Correct Choice')
                else :
                    self.wronganswers += 1 
                    print(f'Invalid Answer \n\t Correct Choice is {correct_choice}')

            
            input_thread = threading.Thread(target=getAnswer)
            input_thread.start() 

            input_thread.join(timeout=90)

            if input_thread.is_alive():
                print("\nTime is up! Moving to the next question.\n")
                self.unattempted += 1 

        print('Your Total Score is : ' , self.score , '/10')
        print('Total Wrong answers attempted : ' , self.wronganswers , '/10')
        print('Total unattempted Questions is : ' , self.unattempted , '/10')
        self.Qualified()

    def Qualified(self) : 

        if self.score >= 6 :
            print(f'Congratulations {self.username}! You are Qualified in you Quiz')
        else : 
            print(f'Sorry {self.username} in order to announce that You are not Qualified in this Quiz ! Better luck next time.')








if __name__ == '__main__':
    obj = QuizGame()
