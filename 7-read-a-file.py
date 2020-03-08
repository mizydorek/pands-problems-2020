# Maciej Izydorek
# Reads a text file entered by user and outputs the number of e's it contains.
# module that allows to specify file name from the command line 
# found on stack overflow https://stackoverflow.com/questions/7033987/python-get-files-from-command-line
import fileinput

# reads file name entered by user and stores in filename variable
# filename =  input('Enter text file name: ')
# counter variable to count e's in txt file 
counter = 0

# with open... function to open file specified by user who typed the name of file
#with open(filename, 'r') as reader:
 #   lines = reader.readlines()
  #  for line in lines:
   #     for letter in line:
    #        if letter == 'e':
     #           counter += 1
      #  print(counter)

# for loop to get lines from the text and inner loop to get every letter from line 
# if statement to count how many e's in the file 
for line in fileinput.input():
    for letter in line:
        if letter == 'e':
            counter += 1
print(counter)  
