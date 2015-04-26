fw = open('t23.txt', 'w')
fw.write('Writing some stuff in my text file \n')
fw.write('I like backon\n')
#always close files when done with them
fw.close()

fr = open('t23.txt', 'r')
text = fr.read()

print(text)
fr.close()