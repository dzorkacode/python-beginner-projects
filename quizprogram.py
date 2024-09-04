quiz={"question1":{"question":"What is the capital of Ghana?", "answer":"Accra"},
      "question2":{"question":"What is the capital of Togo?", "answer":"Lome"},
      "question3":{"question":"What is the capital of Cote D'Ivoire?", "answer":"Yamoussoukro"},
      "question4":{"question":"What is the capital of Burkina Faso?", "answer":"Ouagadougou"},
      "question5":{"question":"What is the capital of Benin?", "answer":"Porto Novo"},
      "question6":{"question":"What is the capital of Nigeria?", "answer":"Abuja"},
      "question7":{"question":"What is the capital of Gambia?", "answer":"Banjul"},
      "question8":{"question":"What is the capital of Gabon?", "answer":"Libreville"},
      "question9":{"question":"What is the capital of Algeria?", "answer":"Algiers"},
      "question10":{"question":"What is the capital of Malawi?", "answer":"Lilongwe"},}

score=0

for key,value in quiz.items():
    print(value['question'])
    answer=input("Answer? ")

    if answer.lower()==value['answer'].lower():
        print('Correct')
        score+=1
        print(f"Your score is: {score}")
        print('')
    else:
        print('Wrong')
        print(f"The answer is: {value['answer']}")
        print('')
    
print(f'You answered {score} out of 10 questions correctly.')
print(f'Your scored {int((score/10)*100)}%')