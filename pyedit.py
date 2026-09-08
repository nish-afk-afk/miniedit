#!/usr/bin/python3

print("Welcome To Miniedit")

file_path = input("enter the filepath of the file you want to edit: ")
if file_path in ["quit", "q", "Q"]:
    exit()

open(file_path)

opened_file = open(file_path)

while True:
    command = input("please name the command you need to execute:")

    if command in ["quit", "q", "Q"]:
        break

    if command in ["read", "r", 'R']:

        print(opened_file.readlines())

    if command in ["edit", "e", "E"]:
        doc = opened_file.readlines()
        for line in doc:
            print(line)
        current_row = 0     
    

        while True:
            
            line = input(": ")
            if line in ["done"]:
                break


            if line.startswith("goto"):
                current_row = int(line.split()[1]) - 1
                newline = input(":n ")
                doc[current_row] = newline + "\n"


            doc.append(line + "\n")

        active_file = open(file_path, "w")
        
        for line in doc:
            active_file.write(line)
