from modules import read_content as content

menu = """
----- Text to Speech -----
1. Read an article
2. Read a text file
3. Enter text manually
4. Exit
"""

while True:
    option = input("Enter an option (1-4): ")

    match option:
        case "1":
            print("##### Read an article #####")

            # URL of the article to convert to audio
            url = input("Enter the URL of the article: ")
            print("\nReading the article, please wait...")

            # Create an instance of the ReadContent class
            reader = content.ReadContent(url)
            reader.read_content()

            # Add a delay to avoid the program from closing immediately
            input("Press Enter to continue...")
            print(menu)

        case "2":
            print("##### Read a text file #####")
            # Path of the text file to read
            file_path = input("Enter the path of the text file (example.txt): ")
            
            # Create an instance of the ReadContent class
            reader = content.ReadContent(file_path, is_url=False)
            reader.read_content()

            # Add a delay to avoid the program from closing immediately
            input("\nPress Enter to continue...")
            print(menu)

        case "3":
            print("##### Enter text manually #####")
            text = input("Enter the text you want to convert to speech: ")

            # Create an instance of the ReadContent class
            reader = content.ReadContent()
            reader.add_manual_text(text)

            # Read the manually entered text
            print("Reading text...")
            reader.read_content()

            # Add a delay to avoid the program from closing immediately
            input("\nPress Enter to continue...")
            print(menu)

        case "4":
            print("Exiting the program...")
            break

        case _:
            print("Enter a valid option.")
            print(menu)