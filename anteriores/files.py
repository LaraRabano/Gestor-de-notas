############################################
## Files



#########################
## Open (Read Mode)

path = "./example.txt"
# write_file = open(path, mode="r")

# lines = write_file.readlines()

# for line in lines:
#     print(line[:-1])

# write_file.close()


#########################
## Open (Write Mode)


path = "./example.txt"
# write_file = open(path, mode="w")

# name = "Lara"
# working = "Software Developer"
# text = f"{name} is working as a {working}"

# write_file.write(text)

# write_file.close()



#########################
## Open (Append Mode)


path = "./example.txt"
write_file = open(path, mode="a")

write_file.write("\nNow you have two lines!")

write_file.close()



#########################
## Context manager


path = "./example.txt"

with open(path, mode="r") as write_file:
    print(write_file.read())

print("File is closed")



##############################
## EXERCISE: Build a quiz system

"""
Build something useful: a quiz, system, using what we've just learnt.

Our quiz system will load data from a text file name 'questions.txt', whose format is like this:

    1+1=2
    2+2=4
    7-4=3


As you can tell, each line represents a Q&A, where questions and answer are separated by a '='.
Your application must:

    - Load the Q&As from 'questions.txt'
    - For each Q&A, prompt the user with the question and expect an input from the user as the answer before moving to the next question.
    For example, for the sample file provided above, it should print '1+1=', and then wait for the user input their answer.
    - You need to keep track of the answers, and after the user answers all the questions, you need to store their grade into a file 'result.txt'
    - The format of the grade should be 'Your final score is {n}/{m}.', where {n} and {m} should be replaced by the number of correct answers and total number os questions respectively.



    1. Get all information from file
    2. Print information so I know what I have
    3. Print only the questions from the information
    4. Ask the user for the answers for each question
    5.
    6.
    7.

"""
