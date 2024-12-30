# https://docs.google.com/spreadsheets/d/1zT6bIv6JRV-yVrbYryKk6LuSbpgYSX3KVsckIqVhrWU/edit?usp=sharing

import random

def suggest_lie(dice): 
    """Bedenkt een geloofwaardige en betere leugen op basis van je huidige worp."""
    faces = ['A', 'K', 'Q', 'J', '10', '9']
    counts = {face: dice.count(face) for face in faces}
    
    # Zoek de meest voorkomende kaart in je echte worp
    best_face = max(counts, key=counts.get)
    highest_count = counts[best_face]
    
    # Als je al een goede worp hebt, doe alsof het nóg beter is
    if highest_count >= 3:  # Bijvoorbeeld, je hebt een Three-of-a-Kind
        lie = [best_face] * 5  # Doe alsof je een Five-of-a-Kind hebt
    else:
        # Liegen naar een betere plausible hand
        lie = [best_face] * 3 + [faces[(faces.index(best_face) + 1) % len(faces)]] * 2  # Full House
    
    return lie

def poker_dice_liar():
    print("Welkom bij Poker Dice Lieg-helper!")
    
    while True:
        # Vraag de gebruiker om hun huidige worp in te voeren
        dice = input("Voer je dobbelstenen in, gescheiden door spaties (bijv. A K Q Q J): ").split()
        
        # Controleer invoer
        if len(dice) != 5 or not all(d in ['A', 'K', 'Q', 'J', '10', '9'] for d in dice):
            print("Ongeldige invoer. Voer precies 5 dobbelstenen in met correcte waarden (A, K, Q, J, 10, 9).")
            continue
        
        # Laat het programma kiezen of het liegt of de waarheid vertelt
        tell_truth = random.choice([True, False])
        
        if tell_truth:
            print("Het programma kiest om de waarheid te vertellen.")
            result = dice
        else:
            print("Het programma kiest om te liegen.")
            result = suggest_lie(dice)
        
        print("Jouw echte worp:", dice)
        print("Het programma zegt:", result)
        
        # Vraag of de gebruiker door wil gaan
        again = input("Wil je nog een keer spelen? (ja/nee): ").lower()
        if again != 'ja':
            print("Bedankt voor het spelen!")
            break

# Start het programma
poker_dice_liar()
