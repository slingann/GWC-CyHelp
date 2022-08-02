# CyHelp Starter Code
cybersecurityBirthYear = 1970

# Greets user
print("Hello! I'm CyHelp.")
userName = input("What's your name?\n")
print("Nice to meet you, " + userName + "!")

#Recounts start of Cybersecurity

currentYear = input("\nWhat year is it?\n")
timePassed = int(currentYear) - cybersecurityBirthYear
print("Wow! That means it has been " + str(timePassed) +
      " years since Cybersecurity began!")

print(
    "The field of Cybersecurity started in the 1970s when more and more information started being stored on computer systems and networks!"
)
input("\nPress enter to continue.\n")

# Describes Cybersecurity
print(
    "Cybersecurity refers to the practices that people use to protect computer systems and networks from digital threats."
)
print(
    "These people can be governments, nations, companies, community organizations, and individuals.\n"
)

# Introduces CIA Triad
print(
    "The CIA Triad is the model used to discuss cybersecurity. CIA stands for confidentiality, integrity, and availability."
)
print("Would you like to learn about the CIA Triad?")
giveInfo = input("Type 'yes' or 'no'.\n")

# Explains pillars of CIA Triad
while giveInfo.lower() == "yes":
    print(
        "What would you like to learn more about? Enter the letter of the following options:\n(a) confidentiality\n(b) integrity\n(c) availability\n(d) none"
    )
    topic = input()

    if topic.lower() == "a":
        print("\nConfidentiality ensures data is private.")

    elif topic.lower() == "b":
        print(
            "\nIntegrity makes sure data has not been tampered with and can be trusted."
        )

    elif topic.lower() == "c":
        print(
            "\nAvailability makes sure authorized people can access the data.")

    elif topic.lower() == "d":
        break

    else:
        print(
            "\nHmm.. that's not an option! Please choose one of the options listed."
        )

# Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")
