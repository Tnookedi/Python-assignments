#Homework2 
#1. create dictionary
def translation(message):
    piratelang = {
        "hello": "ahoy", "sir": "matey", "boy": "matey", "man": "matey",
        "madam": "proud beauty", "officer": "foul blaggart", "the": "th'",
        "my": "me", "your": "yer", "is": "be", "are": "be", "restroom": "head",
        "restaurant": "galley", "hotel": "fleabag inn", "coins": "doubloons",
        "pirate": "buccaneer", "friend": "mate", "you": "ye"
    }
#2. split the string into words
    words = message.lower() and message.split()

#3. translate 
    piratemessage = []
    for word in words:
        if word in piratelang:
            piratemessage.append(piratelang[word])
        else:
            piratemessage.append(word)

#4. join the translated words into a sentence                                                                                                                                                                                          `
    piratemessage = ' '.join(piratemessage)
    return piratemessage

def translated():
#5. get input from user
    message = input("Enter a message: ")
    
#6. translate the input sentence into pirate lang
    piratemessage = translation(message)
    
#7. output the translated sentence
    print("Pirate Translation:", piratemessage)

translated()
