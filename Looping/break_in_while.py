word = input("whats the secret word? ")

while word != "chupacabra" : 
    word = input("whats the secret word? ")
    if word == "chupacabra" :
        break
    
print("You've successfully left the loop.")