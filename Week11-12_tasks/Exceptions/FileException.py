# Exception pt. 1
#try:
#    stream = open("endMe.txt", "rt")
#    for line in stream:
#        line = line.strip()
#    stream.close()
#except Exception as e:
#    print("File can't be opened.", e)

#filename = "countries.txt"
#try:
#    with open(filename, "wt") as file_object:
#        file_object.write(strippedLines[0] / 0)
#except Exception as e:
#    print("File can't be opened.", e)