# Maciej Izydorek
# reads entered string, strips any leading or trailing spaces and 
# outputs in lowercase. Outputs also lenght of the raw string and 
# the normalised one

string = input("Please enter string: ")
normalised = string.strip().lower()

print("That String normalised is : {}".format(normalised))
print("We reduced the input string form {} to {} characters".format(len(string), len(normalised)))