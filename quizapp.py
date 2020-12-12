import database

MENU_PROMPT = """-- Coffee Bean App --
Please choose one of these options:
1) Add a question.
2).find question by topic.
3) Find a question by level.
4) Exit.
Your selection: 
"""


def menu():
    connection = database.connect()
    database.create_tables(connection)

    user_input=input()
    while (user_input == input(MENU_PROMPT)) != "7":
        if user_input == "1":
            prompt_add_question(connection)
        elif user_input == "2":
            prompt_see_question_bytopic(connection)
        elif user_input == "3":
            prompt_see_question_bylevel(connection)
        else:
            print("Invalid option. Please try again.")

def prompt_add_question(connection):
    question = input("Enter question: ")
    level = input("Enter the level: ")
    topic = int(input("Enter the topic "))
    answer = input("Enter answer: ")
    database.add_question(connection, question, level, topic,answer)


def prompt_see_question_bylevel(connection):
    level = input("Enter level: ")
    question = database.get_quiz_by_level(connection, level)

    for qus in question:
        print(f"{question[1]} ({question[2]} - {question[3]}/100")

def prompt_see_question_bytopic(connection):
    level = input("Enter topic: ")
    question = database.get_quiz_by_topic(connection, topic)

    for qus in question:
        print(f"{question[1]} ({question[2]} - {question[3]}/100")


menu()