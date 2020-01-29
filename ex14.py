from sys import argv

script, user_name, loves = argv
prompt = 'Answer:'

print(f"Hi {user_name}, im the script {script}")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have {user_name}?")
computer = input(prompt)

print(f"{user_name} likes {likes}, lives in {lives},and has a computer {computer}, loves {loves}")
