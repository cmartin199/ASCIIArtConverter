# Decoding a text file into ascii art
# 17007981      Christopher Martin
#
readFile = open("ascii vals.txt", "r")
writeFile = open("ascii art.txt", "w")
EOF = False
while not EOF:
    line = readFile.readline()
    text=[]

    if line != "":
        #print line
        line=line.split(",")
        line.pop(-1)

        #print line

        for char in line:
            i=int(char)
            #print i
            text.append(chr(i))
            #print text
        text= ''.join(text)# this joins the text into a string
        #print text
        #len (text)
        text = text.replace("#", " ")
        #text= text.replace(",", "")
        text=text.rstrip("\n")  #  This was done to remove the white space between lines and make the picture look more complete when being printed, but it will also stop the text file from being properly writen to so needs to be hashed out before the file is run.

        print (text)
        #print len(text)
        for char in text:
            strText=str(char)
            writeFile.write(strText)
    else:

        EOF= True
#writeFile.write("\n")
writeFile.close()

'''
        for char in line:
            art = str(chr(char))# + ","
            writeFile.write(art)
        print line
    else:
        EOF = True
   # writeFile.write("\n")


while not EOF:
    line = readFile.readline()

    if line == "":  EOF = True
    else:
        #line = line.replace("#", " ")
        print line

        for char in list(line):
            ascii = str(ord(char)) + ","
            writeFile.write(ascii)

    writeFile.write("\n")
'''
