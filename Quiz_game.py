def ask_question(question, correct_answer):
    answer = input(question + " ").strip().capitalize()
    if answer == correct_answer:
        return True
    else:
        return False

score = 0

questions = [
    ("what is the capital of Nigeria?", "Abuja"),
    ("what is 2 + 2?", "4"),
    ("who is the president of Nigeria?", "Bola Ahmed Tinubu"),
    ("what is the capital of France?", "Paris"),
    ("what is the capital of Germany?", "Berlin"),
    ("what is the capital of Italy?", "Rome"),
    ("what is the capital of Spain?", "Madrid"),
    ("what is the capital of Portugal?", "Lisbon"),
    ("what is the capital of Greece?", "Athens"),
    ("what is the capital of Turkey?", "Ankara"),
    ("what is the capital of Egypt?", "Cairo"),
    ("what is the capital of South Africa?", "Pretoria"),
    ("what is the capital of Kenya?", "Nairobi"),
    ("what is the capital of Ghana?", "Accra"),
    ("what is the capital of Senegal?", "Dakar"),
    ("what is the capital of Morocco?", "Rabat"),
    ("what is the capital of Tunisia?", "Tunis"),
    ("what is the capital of Algeria?", "Algiers"),
    ("what is the capital of Libya?", "Tripoli"),
    ("what is the capital of Sudan?", "Khartoum")
]
for number, (question, correct_answer) in enumerate(questions, start=1):
    print(f"Question {number}: {question}")
    result = ask_question(question, correct_answer)
    if result:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is:", correct_answer)



print("your score is: ", score, "out of", len(questions))