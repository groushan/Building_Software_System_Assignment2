# fortune.py - Version v1.0

def main():
    print("🔮 Welcome to Roushan's Fortune Teller (21JE0783) 🔮")
    mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

    if mood == "happy":
        print("✨ Your fortune: Great things await you, Keep smiling. ✨")
    elif mood == "sad":
        print("✨ Your fortune: Tough times never last, but tough people do. ✨")
    elif mood == "neutral":
        print("✨ Your fortune: Balance is key. Embrace the calm. ✨")
    else:
        print("😕 Sorry, I don't have a fortune for that mood.")

if __name__ == "__main__":
    main()
