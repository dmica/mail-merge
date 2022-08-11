#Create a letter using starting_letter.txt
with open("Input/Letters/starting_letter.txt", mode="w") as file:
    file.write("Dear [name],\n\nYou are invited to my birthday this Saturday.\n\nHope you can make it!\n\nMaya")

#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
names = []

file_names = open("Input/Names/invited_names.txt", "r")
names = file_names.readlines()

for name in names:
    stripped_name = name.strip()
    letter_name = name.replace("[name]", stripped_name)

    with open(f"Output/ReadyToSend/letter_for{letter_name}.txt", mode="w") as file:
        file.write(f"Dear {letter_name},\n\nYou are invited to my birthday this Saturday.\n\nHope you can make it!\n\nMaya")
