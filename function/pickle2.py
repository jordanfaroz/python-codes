

'''exampleobj = {'python':3, 'kde':5, 'windows':10}

fileobj = open('file.obj', 'wb')
pickle.dump(exampleobj,fileobj)
fileobj.close()'''
import pickle

# take user input to take the amount of data
number_of_data = int(input('Enter the number of data : '))
data = []

# take input of the data
for i in range(number_of_data):
    raw = input('Enter data '+str(i)+' : ')
    data.append(raw)

# open a file, where you ant to store the data
file = open('important', 'wb')

# dump information to that file
pickle.dump(data, file)

# close the file
file.close()