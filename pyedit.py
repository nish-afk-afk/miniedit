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

        while True:
            
            line = input(": ")
            if line in ["done"]:
                break
            doc.append(line)
