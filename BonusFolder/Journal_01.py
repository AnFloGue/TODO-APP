date = input(f"Enter today's date ").lower().strip()
mood = input(f"How are you feeling today from 1 to 10? ").lower().strip()
thoughts = input(f"Write a files entry for today: ").lower().strip()
with open("files/journal.txt", "a") as journal_file:
    journal_file.write(f"Date: {date}\nMood: {mood}\nNew entry: {thoughts}\n\n")
    journal_file.writelines(f"Date: {date}\nMood: {mood}\nNew entry: {thoughts}\n\n")
