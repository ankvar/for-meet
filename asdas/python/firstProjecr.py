import random
import datetime

def chatbot():
    print("Hello! I'm Ankvar's ChatBOT!")
    while True:
        user_input = input("You: ")
        user_data = {}
        faq_database = {}
        database = {}
        
        a = 0
        b = 0

        if user_input.lower() in ["hello", "hello there", "hey", "good morning", "gm", "good evening", "good night", "gn"]:
            randomanswer = ["hello, can I help You?", "hello, how am I help for You?", "Hey, what do You need?", "Hello, what do You need, from the internet?"]
            print("ChatBOT: " + random.choice(randomanswer))
        elif user_input.lower() in ["what's the date?", "whats the date"]:
            today = datetime.date.today()
            print("ChatBOT: Today is " + today.strftime("%Y-%m-%d") + ".")
        elif "my name is" in user_input.lower():
            user_name = user_input.lower().replace("my name is", "").strip()
            user_name = user_name.capitalize()
            user_data["name"] = user_name
            print("Hello " + user_name)    
        elif user_input.lower() in["whats your opinion?"]:
            print("Sorry but I don't have any opinion, because I am an AI!")   
        elif user_input.lower() in faq_database:
                print("ChatBot: "+ faq_database[user_input.lower()])
        elif user_input.lower() in["i love you"]:
            print("I Belive you, but I am an AI, and I dont have feelings like peapole.")
        elif user_input.lower() in database:
            print("ChatBot: "+ database[user_input.lower()])    
        elif user_input.lower() in["i understand"]:
            print("Thank you, for your understand. Can I help you?")
        elif user_input.lower() in["osszeadas"]:
            print("Please type 2 numbers ")
            avalue = int(input("A's Value: "))
            bvalue = int(input("B's Value: "))
            print(avalue + bvalue)    
        elif user_input.lower() in["kivonas"]:
            print("Please type 2 numbers ")
            avalue = int(input("A's Value: "))
            bvalue = int(input("B's Value: "))
            print(avalue - bvalue)    
        elif user_input.lower() in["szorzas"]:
            print("Please type 2 numbers ")
            avalue = int(input("A's Value: "))
            bvalue = int(input("B's Value: "))
            print(avalue * bvalue)    
        elif user_input.lower() in["osztas"]:
            print("Please type 2 numbers ")
            avalue = int(input("A's Value: "))
            bvalue = int(input("B's Value: "))
            print(avalue / bvalue)
        elif user_input.lower() in["create me a map"]:
            rows = int(input("How many rows?: "))
            columns = int(input("How many columns?: "))
            symbols = input("Enter a symbol to use!: ")      
            for i in range(rows):
                for j in range(columns):
                    print(symbols, end="")
                print()
        else:
            randomanswer = ["Excuse me! Can You repeat?", "I don't understand You!", "I can't answer that, ask something else!"]
            print("ChatBOT: " + random.choice(randomanswer))
# chatbot()