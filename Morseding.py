
def main():
    translation=False
    mode=0
    try:
        translation=bool(int(input("Enter 0 for training and 1 for translation")))
    except:
        print("Invalid Input. Training mode has been selected by default")
    