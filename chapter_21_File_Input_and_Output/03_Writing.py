my_list = [i**2 for i in range(1,11)]

my_file = open("output.txt", "r+")

# Add your code below!
for e in my_list:
    my_file.write(str(e) + "\n")

my_file.close()