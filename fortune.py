# fortune.py - Version v1.1

import random

def main():
    print("🔮 Welcome to Roushan's Fortune Teller (21JE0783) 🔮")
    mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()

    fortunes = {
        "happy": [
            "Great things await you, Keep smiling.",
            "Happiness is contagious—spread it around!",
            "Your joy lights up the path for others."
        ],
        "sad": [
            "Tough times never last, but tough people do.",
            "Storms make trees take deeper roots.",
            "Roushan believes in you. Better days are near."
        ],
        "neutral": [
            "Balance is key. Embrace the calm.",
            "Still waters run deep—stay thoughtful.",
            "Sometimes no news is good news."
        ],
        "stressed": [
            "Breathe deeply—clarity will come.",
            "You're stronger than you think.",
            "This too shall pass. Relax and reset."
        ]
    }

    if mood in fortunes:
        print("✨ Your fortune:", random.choice(fortunes[mood]), "✨")
    else:
        print("😕 Sorry, I don't have a fortune for that mood.")

if __name__ == "__main__":
    main()
