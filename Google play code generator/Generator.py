import random

print("Welcome to the Google Play code generator!")
while True:
    user_input = input("User: ")

    if user_input.lower() == "default":
    # generates the default 25 codes    
        uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits = "0123456789"

        upper, nums = True, True

        all = ""

        if upper:
            all += uppercase_letters

        if nums:
            all += digits

        length = 4
        amount = 25
        
        for a in range(amount):
            for x in range(1):
                output = "".join(random.sample(all, length))

            for y in range(1):
                output1 = "".join(random.sample(all, length))

            for z in range(1):
                output2 = "".join(random.sample(all, length))

            for l in range(1):
                output3 = "".join(random.sample(all, length))

            print(f'{output}{output1}{output2}{output3}')

    elif user_input.lower() == "enable auto mode":
    # generates 500 codes into a txt file
        uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits = "0123456789"

        upper, nums = True, True

        all = ""

        if upper:
            all += uppercase_letters

        if nums:
            all += digits

        length = 5
        amount = 500
        
        for a in range(amount):
            for x in range(1):
                autooutput = "".join(random.sample(all, length))

            for y in range(1):
                autooutput1 = "".join(random.sample(all, length))

            for z in range(1):
                autooutput2 = "".join(random.sample(all, length))

            for l in range(1):
                autooutput3 = "".join(random.sample(all, length))

            autooutputfinal = (f'{autooutput}{autooutput1}{autooutput2}{autooutput3}')

            with open('codes.txt', 'a') as f:
                f.write('\n')
                f.write(autooutputfinal)

        print("Successfully written the codes into the file")
            
    elif user_input.lower() == "custom":
    # generates a custom amount of codes
        custom_input = input("Enter the amount of codes you want to generate: ")
        custom_input = int(custom_input)
        
        uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits = "0123456789"

        upper, nums = True, True

        all = ""

        if upper:
            all += uppercase_letters

        if nums:
            all += digits

        length = 5
        amount = custom_input
        
        for a in range(amount):
            for x in range(1):
                customoutput = "".join(random.sample(all, length))

            for y in range(1):
                customoutput1 = "".join(random.sample(all, length))

            for z in range(1):
                customoutput2 = "".join(random.sample(all, length))

            for l in range(1):
                customoutput3 = "".join(random.sample(all,length))

            print(f'{customoutput}{customoutput1}{customoutput2}{customoutput3}')

        print(f'Successfully generated {amount} codes!')

    elif user_input.lower() == "quit":
        break

    elif user_input.lower() == "open codes file":
        def read_text_file(file_path):
            try:
                with open(file_path, "r") as file:
                    content = file.read()
                    return content
            except FileNotFoundError:
                print(f"File '{file_path}' not found.")
                return None

        # Example usage:
        file_path = "codes.txt"  # Replace with the path to your text file
        file_content = read_text_file(file_path)
        print("Successfully read content.")
        if file_content:
            print("File content:")
            print(file_content)

    elif user_input.lower() == "wipe codes file":
        with open('codes.txt', 'w') as f:
            f.write("")            
            print("Successfully wiped codes file.")

    else:
        break
