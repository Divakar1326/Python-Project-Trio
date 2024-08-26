import re #re library is used to read raw strings
import random # to select random values
from datetime import datetime # as told to check date and time
jokes=[ # Define some jokes and fun facts
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the math book sad? Because it had too many problems.",
    "why don,t not some couples go to the gym? Because some relationshipsdon not work out.",
    "Did you hear about the restaurant on the moon? Great food, no atmosphere.",
    "why don,t not skeletons fight each other? Theydon not have the guts.",
    "What do you call fake spaghetti? An impasta!",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "What do you get when you cross a snowman and a vampire? Frostbite.",
    "why don,t not scientists trust atoms? Because they make up everything!",
    "why don,t not oysters share their pearls? Because they are shellfish.",
    "What do you call cheese that isn't yours? Nacho cheese.",
    "Why did the bicycle fall over? Because it was two-tired.",
    "What did the grape do when he got stepped on? Nothing but let out a little wine!",
    "How does a penguin build its house? Igloos it together.",
    "Why did the golfer bring extra pants? In case he got a hole in one.",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do cows wear bells? Because their hornsdon not work.",
    "Why couldn nt the leopard play hide and seek? Because he was always spotted.",
    "What is orange and sounds like a parrot? A carrot.",
    "Why do ducks have feathers? To cover their butt quacks.",
    "why don,t not programmers like nature? It has too many bugs.",
    "How many tickles does it take to make an octopus laugh? Ten tickles.",
    "Why do seagulls fly over the sea? Because if they flew over the bay, they wouldd be bagels.",
    "Why was the big cat disqualified from the race? Because it was a cheetah.",
    "what is brown and sticky? A stick.",
    "why don,t not some fish play piano? Because you can nt tuna fish.",
    "Why was the broom late? It swept in.",
    "Why did the coffee file a police report? It got mugged.",
    "why don,t not you ever see elephants hiding in trees? Because they are so good at it.",
    "Why did the scarecrow become a successful neurosurgeon? He was outstanding in his field.",
    "Why are ghosts bad at lying? Because they are too transparent.",
    "why don,t not some couples go to the gym? Because some relationshipsdon not work out.",
    "Why did the tomato turn red? Because it saw the salad dressing.",
    "What do you call a factory that makes good products? A satisfactory.",
    "why don,t not ants get sick? Because they have tiny ant-bodies.",
    "Why did the mushroom go to the party alone? Because he is a fungi.",
    "Why are elevator jokes so good? They work on many levels.",
    "Why did the banana go to the doctor? Because it wasnt peeling well.",
    "Why was the math book sad? It had too many problems.",
    "Why was the stadium so cool? It was filled with fans.",
    "Why did the chicken join a band? Because it had the drumsticks.",
    "Why don not eggs tell jokes? They would crack each other up.",
    "Why do bees have sticky hair? Because they use honeycombs.",
    "Why don not skeletons fight each other? They don not have the guts.",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "Why do vampires seem sick? Because theya re always coffin.",
    "Why did the golfer bring extra pants? In case he got a hole in one.",
    "What do you call fake spaghetti? An impasta!",
]# jokes are made as list
fun_facts={
    'technology':[
        "The first computer virus was created in 1983.",
        "The first 1GB hard drive, announced in 1980, weighed over 500 pounds.",
        "The first known computer programmer was Ada Lovelace in the 1800s."
    ],
    'history':[
        "The Great Wall of China is the only man-made structure visible from space.",
        "The shortest war in history lasted 38 to 45 minutes.",
        "The oldest known living tree is over 5,000 years old."
    ],
    'science':[
        "Water can boil and freeze at the same time in a process called triple point.",
        "Bananas are berries, but strawberries are not.",
        "Octopuses have three hearts and blue blood."
    ]
}# fun facts are declered as dict data type
basic_responses={
    r'hi|hello|hey':'Hello! what is your name?',
    r'how are you':'I am doing great! How about you?',
    r'what is your name':'I am ChatBot, your virtual assistant.',
    r'bye|goodbye':'Goodbye! Have a wonderful day!',
    r'help':'I am here to help you. You can ask me about our services, working hours, or any general queries.',
    r'what can you do':'I can answer your questions, tell you a joke, share a fun fact, and more.',
    r'how to use this service':'Using our service is easy! Just ask me any question you have, and I will do my best to assist you.',
    r'where are you located':'We are located at 123 Main Street, Anytown, USA.',
    r'contact':'You can contact us via email at support@example.com or call us at (123) 456-7890.',
    r'fun fact':'Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.',
    r'quote':'Here is a quote for you: "The best way to predict the future is to invent it." - Alan Kay',
    r'time':'Sorry, I cannot provide the current time right now. But you can check it on your device!',
    r'date':'Sorry, I cannot provide the current date right now. But you can check it on your device!',
    r'weather':'I am not equipped to provide real-time weather updates. You can check the weather on a dedicated weather app or website.',
    r'who created you':'I was created by a team of developers who love AI and technology!',
    r'how old are you':'I am as old as the code that runs me. In a way, I am timeless!',
    r'can you dance':'I can’t dance, but I can certainly imagine a great dance!',
    r'joke':random.choice(jokes),
}#here the responces also declerd as dic type and random file is used to pick one joke when the key is called
user_name=""#declerd globall
def get_fun_fact(category):# if catagory match print fact
    if category in fun_facts:
        return random.choice(fun_facts[category])
    else:
        return "I don't have any fun facts for that category."
def chatbot_response(user_input):
    global user_name #used to make user name global
    # Greet and ask for name if not known
    if not user_name:
        if re.search(r'hi|hello|hey',user_input,re.IGNORECASE):# if name not set search for key and ask for name
            return "Hello! what is your name?"
        elif re.search(r'my name is (.*)',user_input,re.IGNORECASE):#if name is told . capters any any values given and groups them and store them as user name using group
            user_name=re.search(r'my name is (.*)',user_input,re.IGNORECASE).group(1)
            return f"Nice to meet you,{user_name}!"
        else:#ask for user name
            return "Hello! what is your name?"
    # Respond to known user
    if re.search(r'my name is (.*)',user_input,re.IGNORECASE):#if new name is told overwrit username
        user_name=re.search(r'my name is (.*)',user_input,re.IGNORECASE).group(1)
        return f"Nice to meet you,{user_name}!"
    elif re.search(r'call me (.*)',user_input,re.IGNORECASE):#search for alter natives to store user name and overwrite it if told
        user_name=re.search(r'call me (.*)',user_input,re.IGNORECASE).group(1)
        return f"Okay, I'll call you {user_name} from now on."
    # Respond with basic responses
    for pattern,response in basic_responses.items():#items used to pair each key and element to one tuple
        if re.search(pattern,user_input,re.IGNORECASE):#search for given keys from user input ignoring case   
            return response#if found return responce
    # Check for fun fact requests
    if re.search(r'fun fact about (technology|history|science)',user_input,re.IGNORECASE):# if no patten check for fun fact
        category=re.search(r'fun fact about (technology|history|science)',user_input,re.IGNORECASE).group(1)#using group to match the string prited in input and store in catagory
        return get_fun_fact(category)#ruch alredy defined function
    return "I'm sorry, I don't understand that. Can you please rephrase or ask something else?"#ask user to rephrase its as no match is found
def time_based_greeting():# give a grettings with output
    current_hour=datetime.now().hour
    if current_hour<12:#condition for morning
        return "Good morning!"
    elif 12<=current_hour<18:##condition for afternoon
        return "Good afternoon!"
    else:
        return "Good evening!"
def main(): #defining main function
    global user_name #acess user name
    print(f"ChatBot:{time_based_greeting()} I am ChatBot. Type 'exit' to end the conversation.")#wecoming message from chat bot
    while True:#if there is a responce run the loop
        user_input=input("You: ")#getting input from user
        if user_input.lower()=='exit':#condition to exit the conversation
            print("ChatBot: Goodbye! Have a wonderful day!")#end message
            break#end program
        response=chatbot_response(user_input)#else use function to give appropriate responce
        print(f"ChatBot:{response}")#print responce as chat bot
main()#main fuction is called and exicuted


