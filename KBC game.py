from question import QUESTIONS

def isAnswerCorrect(index,answer):
    return True if answer == QUESTIONS[index]["answer"] else False      

def lifeLine(idx):
    k = QUESTIONS[idx]["answer"]
    if k == 1 or k ==2:
        return (1,2)    
    else:
        return (3,4)
            
def kbc():
    print("\n","~"*10, "Your Welcome in the KBC Game ","~"*10 ,"\n")
    lifeline = 4
    money = 0
    
    for i in range(15):
        print("\n\tQuestion",1+i,":", QUESTIONS[i]["name"] ,"\t money :",QUESTIONS[i]["money"] ,"; # lifeline :",lifeline)
        print("\t\tOptions:")
        print('\t\t\tOption 1:', QUESTIONS[i]["option1"])
        print('\t\t\tOption 2:', QUESTIONS[i]["option2"])
        print('\t\t\tOption 3:' ,QUESTIONS[i]["option3"])
        print('\t\t\tOption 4:', QUESTIONS[i]["option4"])
        ans = input('\tYour choice ( 1-4 ) : ')
        
        if lifeline == 0 and ans == "lifeline":
            print("\nYou can not have any lifeline so choose (1-4)")
            ans = input('\tYour choice ( 1-4 ) : ')
        elif ans == "lifeline" and i != 14:
            lifeline -= 1
            print("\tYou should choose one option in",lifeLine(i))
            ans = input('\tYour choice : ')
        elif ans == "lifeline" and i==14:
            print("\nYou can't use lifeline for this question , you should choose (1-4)")
            ans = input('\tYour choice ( 1-4 ) : ')
            
        if ans == "lifeline":
            print("\nGame's rules not followed by you")
            print("\ntotal money which you won :",money)
            break
        
        elif ans == "quit":
            print("\nYou quit the game ")
            print("\ntotal money which you won :",money)
            break
        
        if isAnswerCorrect(i, int(ans) ):
            print('\nCorrect !')
            money += QUESTIONS[i]["money"]
            print("\ntotal money which you won :",money)

        else:
            print('\nIncorrect !')
            print("\ncorrect answer : ",QUESTIONS[i]["answer"])
            if 5<=i<=10:
                money += 10000
            if i>10:
                money += 320000 
            print("\ntotal money which you won :",money)
            break
kbc()
    