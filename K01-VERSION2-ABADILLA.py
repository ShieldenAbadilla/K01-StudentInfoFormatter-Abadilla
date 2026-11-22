first_name = str(input("Enter your first name: "))
last_name = str(input("Enter your last name: "))
section = str(input("Enter your section: "))
subject = str(input("Enter your favorite subject: "))

full_name = first_name + " " + last_name

print("Name:", full_name.title())
print("Name code:", full_name.upper())
print("Section:", section.upper())
print("Favorite Subject:", subject.title())
print("Character count in name:", len(full_name))
