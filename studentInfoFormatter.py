firstName = input("Enter First Name: ")
lastName = input("Enter Last Name: ")
sectionName = input("Enter Section: ")
favoriteSubject = input("Enter Favorite Subject: ")
characterCount = len(firstName + lastName)

print("\nOutput:")
print(
    f"Name: {firstName} {lastName}\n" 
    f"Name Code: {firstName} {lastName}\n" 
    f"Section: {sectionName}\n" 
    f"Favorite Subject: {favoriteSubject}\n"
    f"Character Count: {characterCount}"
)
