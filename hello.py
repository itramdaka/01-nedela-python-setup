#!/usr/bin/env python3
from playwright.sync_api import sync_playwright
"""
Interactive Hello World CLI Program
A simple Python CLI to greet users and showcase interactive features
"""

def yyyyy():
    """Main function for the interactive hello world program"""
    
    print("\n" + "=" * 50)
    print("  Welcome to Interactive Hello World CLI!")
    print("=" * 50 + "\n")
    
    # Get user's name
    name = input("What's your name? > ").strip()
    
    if not name:
        name = "Friend"
    
    print(f"\n✨ Hello, {name}! ✨\n")
    
    # Interactive menu
    while True:
        print("What would you like to do?")
        print("1. Greet me again")
        print("2. Tell me a fun fact")
        print("3. Count something")
        print("4. Exit")
        print()
        
        choice = input("Enter your choice (1-4): > ").strip()
        
        if choice == "1":
            print(f"\n👋 Hello again, {name}!\n")
        
        elif choice == "2":
            print("\n🎯 Fun Fact: Python was named after the British comedy group Monty Python!")
            print("   It was created by Guido van Rossum in 1991.\n")
        
        elif choice == "3":
            try:
                limit = int(input("\nHow high should I count? > "))
                print("Counting: ", end="")
                for i in range(1, limit + 1):
                    print(i, end=" ")
                print("\n")
            except ValueError:
                print("❌ Please enter a valid number.\n")
        
        elif choice == "4":
            print(f"\n👋 Goodbye, {name}! Have a great day!\n")
            break
        
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.\n")


    

def test_homepage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://vm.gov.lv")
        
        assert page.title() == "Example Domain"
        
        browser.close()


if __name__ == "__main__":
    test_homepage()