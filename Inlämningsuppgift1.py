word_count = 0   # Initialiserar variablerna
line_count = 0
lines_that_a_word_appears_on = []

print("This script counts lines and words in text files")

while True:     # Loop för att slippa starta om programmet när man skriver fel input
    print("")
    input_file = input("Please input the filename or filepath you would like to use: ")    # Tar input och sparar ner den i en variabel för vidare hantering

    if "." in input_file:   # Fångar om användaren inte skriver en filändelse

        text_file_check = input_file.split(".")[1]      # Delar upp användarens input där det finns en punkt och sparar ner den del av strängen som kommer efter punkten i en variabel

        if text_file_check == "txt":    # Kollar om filändelsen är txt
            try:    # Använder try för att fånga fel i öppningen av filen
                with open(input_file, "r", encoding="utf-8") as f:    # Öppnar filen och använder variablen f för att hantera den (behövde definera encoding för att få filen att läsas korrekt)
                    print("You can count specific words aswell")
                    input_word = input("Enter your word here (case sensitive) or leave blank to count all words and lines: ")

                    if input_word == "":    # Om inget ord specificeras, räknas alla ord och rader
                        for line in f:      # For loop som går igenom varje rad i filen   
                            stripped_line = line.rstrip()     # Skapar en variabel och sparar den nuvarande raden i högertrimmat format (tar bort allt whitespace till höger om radens slut) 
                            all_words_on_line = stripped_line.split()       # En till variabel som delar upp den nuvarande raden med default split på vilken whitespace karaktär som helst
                            word_count += len(all_words_on_line)   # Lägger till antalet "ord" som delats upp från den nuvarande raden och lägger till den i min tidigare deklarerade variabel
                            line_count += 1          # Lägger till 1 för varje rad som loopen går igenom

                        print("The word count is:", word_count)
                        print("The line count is:", line_count)  
                        break   # Avslutar programmet
                    else:
                        for line in f:
                            line_count += 1
                            stripped_line = line.rstrip()
                            all_words_on_line = stripped_line.split() #Separerar raden i ord så att sökningen inte tar upp delar av ett annat ord, exempelvis en sökning på "He" kan annars ta upp ord som "Hell"

                            if input_word in all_words_on_line: # Om det specificerade ordet finns i den nuvarande raden räknas det och raden den var på läggs till i en fördefinerad lista
                                word_count += 1
                                lines_that_a_word_appears_on.append(str(line_count))
                                
                        print("There are", word_count, "instances of", input_word)
                        if word_count > 0:
                            print("They appear on lines:", lines_that_a_word_appears_on)
                        break
            except:
                print("Could not find/open specified file")
        else:
            print("File is not a text file")
    else:
        print("Please include the filetype")
    