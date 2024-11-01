import random
def main():
    morse_to_text = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', 
    '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', 
    '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', 
    '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', 
    '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', 
    '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', 
    '-.-.--': '!', '-....-': '-', '-..-.': '/', '.--.-.': '@', '-.--.': '(', '-.--.-': ')',
    '.-.-.': '+', '-.-.-.': ';', '---...': ':', '.-..-.': '"', '.----.': "'", '...-..-': '$', 
    '.-...': '&', '...---...': 'SOS', '...-.': 'SK', '.-.-.': 'AR', '-...-.-': 'BK', 
    '.-.-.': 'CT', '-.-.-': 'KN', '...-.-': 'VA', '-...-': '=', '........':'ERROR',
    #the following entries are for readability only:
    '/':' ', '':''
    }
    text_to_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', 
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
    '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', 
    '!': '-.-.--', '-': '-....-', '/': '-..-.', '@': '.--.-.', '(': '-.--.', ')': '-.--.-',
    '+': '.-.-.', ';': '-.-.-.', ':': '---...', '"': '.-..-.', "'": '.----.', '$': '...-..-', 
    '&': '.-...', 'SOS': '...---...', 'SK': '...-.', 'AR': '.-.-.', 'BK': '-...-.-', 
    'CT': '.-.-.', 'KN': '-.-.-', 'VA': '...-.-', '=': '-...-', 'ERROR':'........',
    #the following entries are for readability only:
    ' ':'/', '':''
    }
    translation=False
    try:
        translation=bool(int(input("Enter 0 for Training mode and 1 for Translation mode: ")))
    except:
        print("Invalid Input. Training mode has been selected by default")
    mode=modeswitch()
    if(translation & mode>=2):
        print("Invalid input. Try again")
        mode=modeswitch()
    if(translation):
        if(mode==0):
            morseToTextTranslation(morse_to_text)
        else:
            textToMorseTranslation(text_to_morse)
    elif(mode==0):
        morseToTextTraining(morse_to_text)
    elif(mode==1):
        textToMorseTraining(text_to_morse)
    else:
        mixedTraining(morse_to_text,text_to_morse)
def modeswitch():
    #modes:
    #0: Morse to Text
    #1: Text to Morse
    #2: Mixed
    try:
        mode=int(input("Input: 0 for Morse to Text; 1 for Text to Morse; 2 for Mixed(Not available in Translation Mode): "))
        if(mode>=0 & mode<=2):
            return mode
        else:
            print("Invalid input. Try again")
            modeswitch()
    except:
        print("Invalid input. Try again")
        modeswitch()
    
def morseToTextTranslation(dict):
    morse=input("Input morse message with letters separated by spaces and words by slashes: ")
    plainText=""
    nextIndex=morse.find(" ")
    unfinished = True
    while(unfinished):
        if(morse.find(" ")==-1):
            try:
                plainText=plainText+dict[morse]
            except:
                plainText=plainText+'#'
            unfinished=False
            print("This is the corresponding plaintext, '#' represent invalid sequences and/or characters: "+plainText)
        else:
            nextIndex=morse.find(" ")
            try:
                plainText=plainText+dict[morse[:nextIndex]]
            except:
                plainText=plainText+'#'
            morse=morse.removeprefix(morse[:nextIndex+1])
def textToMorseTranslation(dict):
    morse=""
    plainText=input("Input plaintext: ").upper()
    for i in range(len(plainText)):
        try:
            morse=morse + dict[plainText[i]]+" "
        except:
            morse=morse+plainText[i]
    print("This is the corresponding morse code: "+morse)
def morseToTextTraining(dict):
    gameLength=int(input("How many Questions do you want? "))
    score=0
    numberOfGuesses=0
    endcondition=False
    while(not endcondition):
        for w in dict:
            if((random.random()<0.01) & (dict[w]!='') & (dict[w]!='/')):
                if(numberOfGuesses<=gameLength):
                    guess=input("What is the plaintext letter of:"+ w+"? ")
                    if(guess==dict[w] or guess.upper()==dict[w]):
                        score=score+1
                        print("Good Job! Your current score is:"+ str(score))
                    else:
                        print("Wrong! The correct answer would have been:"+dict[w]+", Your current score is:"+str(score))
                    numberOfGuesses=numberOfGuesses+1
                else:
                    endcondition=True
    print("Good Job! You have a score of:"+str(score)+", Your answers are correct "+str(round(score/numberOfGuesses*100,1))+"% of the time!")
def textToMorseTraining(dict):
    gameLength=int(input("How many Questions do you want? "))
    score=0
    numberOfGuesses=0
    endcondition=False
    while(not endcondition):
        for w in dict:
            if((random.random()<0.01) & (dict[w]!=' ') & (dict[w]!='')):
                if(numberOfGuesses<=gameLength):
                    if(input("What is the morse code of:"+ w+"? ")==dict[w]):
                        score=score+1
                        print("Good Job! Your current score is:"+ str(score))
                    else:
                        print("Wrong! The correct answer would have been:"+dict[w]+", Your current score is:"+str(score))
                    numberOfGuesses=numberOfGuesses+1
                else:
                    endcondition=True
    print("Good Job! You have a score of:"+str(score)+", Your answers are correct "+str(round(score/numberOfGuesses*100,1))+"% of the time!")
def mixedTraining(morse_to_text, text_to_morse):
    dict= morse_to_text | text_to_morse
    gameLength=int(input("How many Questions do you want? "))
    score=0
    numberOfGuesses=0
    endcondition=False
    while(not endcondition):
        for w in dict:
            if((random.random()<0.01) & (dict[w]!=' ') & (dict[w]!='')):
                if(numberOfGuesses<=gameLength):
                    if(input("What is the translation of:"+ w+"? ")==dict[w]):
                        score=score+1
                        print("Good Job! Your current score is:"+ str(score))
                    else:
                        print("Wrong! The correct answer would have been:"+dict[w]+", Your current score is:"+str(score))
                    numberOfGuesses=numberOfGuesses+1
                else:
                    endcondition=True
    print("Good Job! You have a score of:"+str(score)+", Your answers are correct "+str(round(score/numberOfGuesses*100,1))+"% of the time!")
main()