#
#Author: Sahil Desai
#Description: This program takes two inputs from the user. The first is name of a text file,
#and second input will be the mode that the program should operate in.
#There will be two modes: suggest or replace mode.
#
def main():
    input_file=input('Enter input file: \n')
    read_file=open(input_file,'r')
    read_data=read_file.readlines() #reads all the lines from the input file
    #print("read data",read_data)
    which_mode=input('Enter spellcheck mode (replace or suggest): \n')
    dictionary=misspell()
    print()
    print('--- OUTPUT ---')
    if which_mode=='replace': #If user gives replace mode
        replace(dictionary,read_data) #Replace function will be called
    else:
        suggest(dictionary,read_data)#Else suggest function

#This function is responsible for open up and read a file names misspellings.txt.
#Assume that this file already exists. This file include information about how
#words are misspelled. This helps to figure out which words are spelled wrong in the input file.
#Takes no paremeters. But returns an dictionary with values in it.
def misspell():
    dictionary={}
    read_file=open('misspellings.txt','r')
    data=read_file.readlines()
    elements=[]
    for i in range (0,len(data)): #This loop strips the new line character
        elements.append(data[i].strip('\n'))
    for j in elements: #To split keys and values
        l=j.split(':')
        value_list=l[1].split(',')
        value=l[0]

        for i in range (0,len(value_list)): #To update/add in the dictionary
            dictionary.update({value_list[i]:value})
        #print("dictionary",dictionary)
    return dictionary

#This is the suggest mode function, the program does not make any changes
#to the text. Insted, it annotate the text with suggestions for how to spell
#words differently. This functions takes two parameters.
    #First is dictionary which stores correct spelling for wrong words.
    #Second is read_data which is contains each lines of the input file.

def suggest(dictionary,read_data):
    key_list=[]
    count=0 #Counts number of wrong spelling
    final_list=[]
    elements=[]
    for i in range (0,len(read_data)): #Go through each line in the file
        elements.append(read_data[i])  #appends the data to elements.
    for j in elements:
        re_store='' # Stores all the words
        pop='' # Updates the capital and re-store in pop
        data='' # Final list is been stored in data
        word_list=j.split(' ') #Stores each word of the line in word_list all as a list
        for i in range (0,len(word_list)): #To check all the words in the dictionary
            if word_list[i][0].isupper(): #Check if the word is upper case
                word_list[i]=word_list[i].lower()
                word_list[i]=word_list[i].strip('\n')
                if word_list[i] in dictionary.keys(): #Check if the word is in the list
                    re_store+=dictionary[word_list[i]]
                    pop+=re_store[0].upper() #Re-Capitalizes the word
                    pop+=re_store[1:] #Appends the rest of the lower case words
                    key_list.append(pop)
                    data+=word_list[i][0].upper()
                    if i==len(word_list)-1: #This if-statment checks if it is the word
                        data+=word_list[i][1:] #then it will bring the cursor on the new line.
                        count+=1
                        data+=' ('+str(count)+')' #Counts number of mistakes found in the file
                        data+='\n'
                        final_list.append(str(count)) #Stores in the final_list
                    else: #This else will contine to the same line
                        data+=word_list[i][1:]
                        count+=1
                        data+=' ('+str(count)+')'
                        final_list.append(str(count))
                        data+=' '
                else: #If the word is not found in the dictionary then it go through
                    data+=word_list[i][0].upper()
                    if i==len(word_list)-1:
                        data+=word_list[i][1:]
                        data+='\n'
                    else:
                        data+=word_list[i][1:]
                        data+=' '
            else: #If the word is not in upper case
                word_list[i]=word_list[i].strip('\n')
                if word_list[i] in dictionary.keys():
                    key_list.append(dictionary[word_list[i]])
                    if i==len(word_list)-1:
                        data+=word_list[i]
                        count+=1
                        data+=' ('+str(count)+')'
                        data+='\n'
                        final_list.append(str(count))
                    else:
                        data+=word_list[i]
                        count+=1
                        data+=' ('+str(count)+')'
                        final_list.append(str(count))
                        data+=' '
                else:
                    if i==len(word_list)-1:
                        data+=word_list[i]
                        data+='\n'
                    else:
                        data+=word_list[i]
                        data+=' '

        print(data,end='')
    print()
    print('--- LEGEND ---')
    for legend  in range (len(key_list)): #displays the each misspell words
            print('('+final_list[legend]+')',key_list[legend])

#This is the replace mode function, this program prints out the contents of the
#input file with the spelling already fixed.
    #First is dictionary which stores correct spelling for wrong words.
    #Second is read_data which is contains each lines of the input file.
def replace(dictionary,read_data):
    elements=[]
    for i in range (0,len(read_data)): #Go through each line in the file
        elements.append(read_data[i])  #appends it to elements
    for j in elements:
        final_data=''
        word_list=j.split(' ')
        for i in range (0,len(word_list)): #To check all the words in the dictionary
            if word_list[i][0].isupper(): #Check if the word is upper case
                word_list[i]=word_list[i].lower()
                word_list[i]=word_list[i].strip('\n')
                if word_list[i] in dictionary.keys(): #Chekc if the word is in the list
                    word_list[i]=dictionary[word_list[i]] #If word found in dictionary
                    final_data+=word_list[i][0].upper()   #it swaps the misspell with correct spell
                    if i==len(word_list)-1: #This if-statment checks if it is the word
                        final_data+=word_list[i][1:] #then it will bring the cursor on the new line.
                    else: #This else will contine to the same line
                        final_data+=word_list[i][1:]
                        final_data+=' '
                else: #If the word is not found in the dictionary then it go through
                    final_data+=word_list[i][0].upper()
                    if i==len(word_list)-1:
                        final_data+=word_list[i][1:]
                    else:
                        final_data+=word_list[i][1:]
                        final_data+=' '
            else: #If the word is not in upper case
                word_list[i]=word_list[i].strip('\n')
                if word_list[i] in dictionary.keys():
                    word_list[i]=dictionary[word_list[i]]
                    if i==len(word_list)-1:
                        final_data+=word_list[i]
                    else:
                        final_data+=word_list[i]
                        final_data+=' '
                else:
                    if i==len(word_list)-1:
                        final_data+=word_list[i]
                    else:
                        final_data+=word_list[i]
                        final_data+=' '

        print(final_data,end='')
        print('')



main()
