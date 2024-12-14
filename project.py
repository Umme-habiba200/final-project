def quiz():
    Questions = {
        "lists are shown by which brackets?":"square brackets",
        "Are tuples changeable?":"no",
        "which shows the value by rounding the value to the nearest integer, / ot //?":"//",
        "can multiple ifs be used as multiple elifs are used?":"yes",
        "does in pascal case each first letter is capatalize?":"yes"

    }
    score=0
    for question , answer in Questions.items():
        print(question) 
        user_Answer=input("your Answer: ") 
        if user_Answer.lower() == answer.lower():
            print("correct")
            score += 1
        else:
            print("incorrect. the Answer is:", answer)
    
    print("\nyour final score is:", score, "/", len(Questions))

quiz()
