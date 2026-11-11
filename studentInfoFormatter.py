firstName = input("Enter First Name: ").strip()
lastName = input("Enter Last Name: ").strip()
sectionName = input("Enter Section: ")
favoriteSubject = input("Enter Favorite Subject: ")
characterCount = len(firstName + " " + lastName)

print("\nFormatted Output:")
print(
    f"Name: {firstName.capitalize()} {lastName.capitalize()}\n" 
    f"Name Code: {firstName.upper()} {lastName.upper()}\n" 
    f"Section: {sectionName.upper()}\n" 
    f"Favorite Subject: {favoriteSubject.capitalize()}\n"
    f"Character Count: {characterCount}"
)
