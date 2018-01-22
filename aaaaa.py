quotes = ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", "On doit pouvoir choisir entre s'écouter parler et se faire entendre."]
user_answer = input("Tapez entrée pour découvrir une autre citation ou B pour quitter le programme.")
if user_answer == "B":
	pass
elif user_answer== "C":
    print("ce pas la bonne reponse")
else: 
    pass
def get_random_item_in(my_list):
    # TODO: get a random number
    item = my_list[0] # get a quote from a list
    print(item) # show the quote in the interpreter
    return item # returned value

user_answer = input ("tapez pour conaitre la citation")

while user_answer != "B":
    print(get_random_item_in(quotes))
    user_answer = input ("tapez entrée pour connaitre une autre citation ou B pour quittez le programme")
for quote in quotes:
    quote.capitalize()
    quotes[3]
    
