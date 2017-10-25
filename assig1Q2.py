#import libraries
import matplotlib as mato
import matplotlib.pyplot as pygraph

characters = list() # list to read ASCII characters
wordsList = list() #list to read file characters
wordsFreq = list() #list to read frequency of characters
xAxis = list() #data for xAxis
yAxis = list() #data for yAxis

#read file
sampleFile = open('sample.txt','r')

#alphabets to compare file characters from
for i in range(32,127): 
    characters.append(chr(i))

while 1: #infinite loop to run until all characters inside file are read
     oneCharacter = sampleFile.read(1)          # read by character
     if not oneCharacter: break #if no more characters left then terminate the loop and go for other                               statements out of the loop 
     wordsList.append(oneCharacter)
 
#convert list into strings 
print (''.join(wordsList))

#compare file list characters to ASCII characters and count frequency 
print("CHaracters ", " Frequency")
for i in range(len(characters)):
    if not wordsList.count(characters[i]) == 0:
      xAxis.append(characters[i])  #all characters in document
      yAxis.append(wordsList.count(characters[i])) #frequency of each character
      if characters[i] == ' ':  
        xAxis[i]  = 'spaces'; #name of space character in histogram
        print("Spaces", " \t ",  wordsList.count(characters[i]))
      else:
        print(characters[i], "\t \t ", wordsList.count(characters[i]))

#count number of labels required for xAxis
barGap = range(0,len(yAxis)) #labeling data for x and y axis (0,1,2,3...) this will count number of elements in frequency array

barGapY = range(0,max(yAxis))
pygraph.title("Frequency Distribution Histogram")

width = 1.0     # gives histogram aspect to the bar diagram, (width of bars for design)

ax = pygraph.axes() #call axis function of matplotlib, for graph axis 
pygraph.yticks(range(min(barGapY), max(barGapY)+1, 10)) #ax.set_yticks(positions) -- range of ticks, its minimum, maximum limit and inmtervals
ax.set_xticks(barGap)  #ax.set_xticks(positions) -- number of ticks or number of values of x axis
ax.set_xticklabels(xAxis) #labels for xAxis values


ax.set_xlabel("File Characters")
ax.set_ylabel("Frequency of Characters")

pygraph.bar(barGap, yAxis, width, color='r')
#pygraph.bar((y,x)|(y axis data), list of frequencies(height of bars, x axis data), width of bars, color)
 
# Set figure width to 12 and height to 9
pygraph.rcParams["figure.figsize"] = 12,9 #(used for different default graph parameters)changes default value of graph width and height

pygraph.show()
#clear buffer, or else data will keep on repeating 
del  wordsList[:] 
sampleFile.close()
