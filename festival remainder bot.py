import datetime

# Dictionary to store festivals { "FestivalName": "YYYY-MM-DD" }
festivals = {
    "Diwali": "2025-10-20",
    "Christmas": "2025-12-25",
    "Holi": "2025-03-14"
}

def display_menu():
    print("\n📅 Festival Reminder Bot")
    print("1. View all saved festivals")
    print("2. Add a new festival")
    print("3. Delete a festival")
    print("4. Check reminders")
    print("5. Exit")

def view_festivals():
    if not festivals:
        print("No festivals saved yet.")
        return
    print("\nSaved Festivals:")
    for fest, date in festivals.items():
        print(f"- {fest}: {date}")

def add_festival():
    name = input("Enter festival name: ").strip()
    date_str = input("Enter date (YYYY-MM-DD): ").strip()
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")  # validate format
        festivals[name] = date_str
        print(f"✅ Festival '{name}' added for {date_str}.")
    except ValueError:
        print("❌ Invalid date format. Use YYYY-MM-DD.")

def delete_festival():
    name = input("Enter festival name to delete: ").strip()
    if name in festivals:
        del festivals[name]
        print(f"🗑 Festival '{name}' deleted.")
    else:
        print("❌ Festival not found.")

def check_reminders():
    today = datetime.date.today()
    print(f"\n🔔 Reminders for {today}:")
    for fest, date_str in festivals.items():
        fest_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        days_left = (fest_date - today).days

        if days_left == 0:
            print(f"🎉 Today is {fest}!")
        elif 0 < days_left <= 7:
            print(f"⏳ {fest} is in {days_left} day(s) on {fest_date}.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            view_festivals()
        elif choice == "2":
            add_festival()
        elif choice == "3":
            delete_festival()
        elif choice == "4":
            check_reminders()
        elif choice == "5":
            print("👋 Exiting Festival Reminder Bot. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
