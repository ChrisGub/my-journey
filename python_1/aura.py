import sys
import time

def clear_screen():
    print("\n" * 50)

def speak_bite():
    """Attempts to play a bite sound or text-to-speech fallback."""
    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say("Chomp! Crunch!")
        engine.runAndWait()
    except ImportError:
        # Fallback if pyttsx3 isn't installed
        if sys.platform == "win32":
            import winsound
            winsound.Beep(400, 150)
            winsound.Beep(300, 150)
        else:
            print("\a") # Standard system bell

def show_donut(state="whole"):
    if state == "whole":
        print(r"""
             .-''''-.
           .'        '.
          /            \

         |     (  )     |
         |              |
          \            /
           '.        .'
             '-____-'
        """) 
    elif state == "bitten":
        print(r"""
             .-''''-.
           .'        '.
          /            \
         |     (  )     \____  (BITE!)
         |               ____)
          \            /
           '.        .'
             '-____-'
        """)
    elif state == "flying":
        print(r"""
                           .   \ | /   .
                             \       /
                        .-''''-. ___
                      .'        '.   -  _
                     /            \      - _  (LAUNCH!!!)

                    |     (  )     |        -
                    |              |       _ -
                     \            /    - _
                      '.        .'
                        '-____-'
        """)

def main():
    clear_screen()
    print("=== WELCOME TO THE DONUT SIMULATOR ===")
    
    # Ask the user to press play
    input("\nPress [ENTER] to Play...")
    
    clear_screen()
    print("--- Your Donut is Ready! ---")
    show_donut("whole")
    
    # Show options
    print("What would you like to do?")
    print("1. Take a bite")
    print("2. Change donut type (Menu)")
    print("3. Launch the donut")
    
    choice = input("\nSelect an option (1-3): ").strip()
    clear_screen()
    
    if choice == "1":
        print("*CHOMP!* You took a bite out of the donut!")
        show_donut("bitten")
        speak_bite()
        time.sleep(2)
        
    elif choice == "2":
        print("=== DONUT MENU ===")
        print("1. Glazed Classic")
        print("2. Chocolate Sprinkle")
        print("3. Jelly Filled")
        print("4. Boston Cream")
        selected_flavor = input("\nPick a new flavor (1-4): ")
        print(f"\nExcellent choice! Your donut is now changing flavors...")
        time.sleep(2)
        
    elif choice == "3":
        print("Ignition... 3... 2... 1...")
        time.sleep(1)
        show_donut("flying")
        print("\nThe donut has launched into deep space!")
        time.sleep(2)
        
    else:
        print("Invalid choice! The donut got confused.")
        time.sleep(1)
        
    clear_screen()
    print("Action finished. Program ending. Goodbye! 🍩")

if __name__ == "__main__":
    main()
