#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


ready_list = []

with open("Input/Names/invited_names.txt") as name_file:
    name_list = name_file.readlines()
    # print(name)

with open("Input/Letters/starting_letter.txt", "r") as starting_letter:
    
    placeholder = starting_letter.read()
    for name in name_list:
        striped_name = name.strip()
        ready = placeholder.replace("[name]", striped_name)
        with open(f"Output/ReadyToSend/{striped_name}", "w") as ready_to_send:
            ready_to_send.write(ready)

