import pandas as pd
import matplotlib.pyplot as plt
import os

# File to store data
DATA_FILE = "fitness_tracker_data.csv"

# Load data from the CSV file or create a new one
def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    else:
        return pd.DataFrame(columns=["Date", "Exercise", "Duration (min)", "Calories Burned"])

# Save data to the CSV file
def save_data(df):
    df.to_csv(DATA_FILE, index=False)

# Add a new exercise log
def add_log(date, exercise, duration, calories):
    """
    Adds a new exercise log entry to the CSV file.
    """
    new_entry = pd.DataFrame({
        'Date': [date],
        'Exercise': [exercise],
        'Duration (min)': [duration],
        'Calories Burned': [calories]
    })
    file_path = os.path.join(os.getcwd(), 'fitness_tracker_data.csv')

    try:
        # Read existing data
        data = pd.read_csv('fitness_tracker_data.csv')
    except FileNotFoundError:
        # If the file doesn't exist, initialize a new DataFrame
        data = pd.DataFrame(columns=['Date', 'Exercise', 'Duration (min)', 'Calories Burned'])

    # Append the new entry
    data = pd.concat([data, new_entry], ignore_index=True)

    # Save back to the CSV file
    data.to_csv('fitness_tracker_data.csv', index=False)
    print("Log added successfully!")


# Display logs
def display_logs():
    global data
    if data.empty:
        print("\nNo logs available.")
    else:
        print("\nExercise Logs:")
        print(data)

# Visualize progress
def visualize_progress():
    global data
    if data.empty:
        print("\nNo data to visualize.")
        return

    data["Date"] = pd.to_datetime(data["Date"])  # Ensure dates are in the correct format
    grouped = data.groupby("Date").sum()  # Group data by date
    grouped.plot(y=["Calories Burned", "Duration (min)"], kind="line", marker="o", figsize=(10, 5))
    plt.title("Fitness Progress Over Time")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.legend(["Calories Burned", "Duration (min)"])
    plt.grid(True)
    plt.show()

# Main menu
def menu():
    while True:
        print("\n=== Fitness Tracker ===")
        print("1. Add Exercise Log")
        print("2. View Logs")
        print("3. Visualize Progress")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            exercise = input("Enter the exercise name: ")
            duration = int(input("Enter the duration (in minutes): "))
            calories = int(input("Enter calories burned: "))
            add_log(date, exercise, duration, calories)
        elif choice == "2":
            display_logs()
        elif choice == "3":
            visualize_progress()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Load or initialize data
data = load_data()

if __name__ == "__main__":
    menu()
