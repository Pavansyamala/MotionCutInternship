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
        self.user = input("Enter y in order to proceed to the  quiz else n  [y/n] : ")
        if self.user == 'y' : 
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
        if understood == 'y':
            self.StartQuiz()
    
    def StartQuiz(self):

        while self.totalQuestions > 0 :

            self.totalQuestions -= 1 
            question = self.questions[self.totalQuestions]
            correct_choice = self.answers[self.totalQuestions]
            print(question)
            def getAnswer():
                answer = input("Enter your Answer : ")
                if answer == correct_choice :
                    self.score += 1
                    print('Correct Choice')
                else :
                    self.score += 0 
                    self.wronganswers += 1 
                    print(f'Invalid Answer \n Correct Choice is {correct_choice}')

            
            input_thread = threading.Thread(target=getAnswer)
            input_thread.start() 

            input_thread.join(timeout=90)

            if input_thread.is_alive():
                print("\nTime is up! Moving to the next question.")
                self.unattempted += 1 
                self.score += 0 

        print('Total Score is : ' , self.score)
        print('Total Wrong answers is : ' , self.wronganswers)
        print('Total unattempted Questions is : ' , self.unattempted)
        self.Qualified()

    def Qualified(self) : 

        if self.score >= 6 :
            print('Congratulations ! You are Qualified in you Quiz')
        else : 
            print('Oops! You are not Qualified in')








if __name__ == '__main__':
    obj = QuizGame()
