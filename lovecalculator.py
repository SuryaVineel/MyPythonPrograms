print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
score1=0
score2=0
final_name = name1.lower()+name2.lower()
#sentence = 'Mary had a little lamb'
score1+=final_name.count('t')
score1+=final_name.count('r')
score1+=final_name.count('u')
score1+=final_name.count('e')

score2+=final_name.count('l')
score2+=final_name.count('o')
score2+=final_name.count('v')
score2+=final_name.count('e')

final=str(score1)+str(score2)
#final_score=int(final)
final_score = int(final)
if (final_score < 10 or final_score>90):
    print(f"Your score is {final_score}, you go together like coke and mentos.")
elif (40<final_score<50):
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}.")
