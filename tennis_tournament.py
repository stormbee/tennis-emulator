
import os                                                   # שימוש רק כדי לרוקן קונסול
import random                                               # שימוש בכל תכונות של רנדום
from time import sleep                                      # בשביל המתנה
SLEEP_TIME=0.1                                              # משתנים כבועים
SETS=3
players=[['Novak Djokovic','22/05/1987',30,510],        
      ['Rafael Nadal','03/06/1986',17,480],
      ['Roger Federer','08/08/1981',27,490],
      ['Dominic Thiem','03/09/1996',14,300],
      ['Kei Nishikori','29/12/1989',23,500],
      ['Alexander Zverev','20/04/1997',18,320],
      ['Stefanos Tsitsipas','12/08/1998',17,450],
      ['Daniil Medvedev','11/02/1996',16,340],
      ['Karen Khachanov','21/05/1996',14,380],
      ['Fabio Fognini','24/05/1987',27,350],  ]

tournaments = [['Australian Open'],                         # רשימה נוספת של תחרויות
               ['French Open'],
               ['Wimbledon'],
               ['US Open'],      ]


pamount = 2 ** random.randrange(1,4)                        # כמות שחקנים בחיזקה 2 בשביל תחרויות

tournament_plist = []                                       # רשימה של שחקנים שמשתתפים בתחרות



def printPlayers(plist,num=1):                              # פונקציה מקבלת רשימה וארך שהוא כמות שחקנים במקרא עם צריך להדפיס כמות מסויימת מתחילת רשימה או מסוף.

    def countSpaces(plist,num,a,b):                         #   פונקציה נוספת במוסיפה רווחים מסודר לכל פירוט של כל שחקן. כמו שם, תאריך לידה, כמות תחרויות , וניקודות. מקבלת ארכים ולפי אותם מדפיסה שחקנים הנדרשים

        for i in range(a,b):                                # לולאה של שורות  
            print(f'{i+1:>2}.',end='')                      # אחרי כל איטרציה מדפיסה מספר של שחקן ברשימה  עם 2מקומות למספר במיקרא עם כמות שחקנים יותר מ-9
            for j in range(len(plist[i])):                  # לולאה של כל רשימת כל שחקן בודד
                if j == 0:                                  # עם מדפיסים שם שלפי סדר זה מקום 0 ברשימה
                    print(f'{plist[i][j]:<20}',end=' ')     # אז מדפיסים עם 20 מקומות שורה
                elif j == 1:                                # עם מדפיסים תאריך לידה שזלפי סדר מקום 1 ברשימה
                    print(f'{plist[i][j]:<12}',end=' ')     # אז מדפיסים עם 12 מקומות שורה
                else:                                       # כל השאר שזה כמות תחרויות וכמות נקודות
                    print(f'{plist[i][j]:<5}',end=' ')      # אז מדפיסים עם 5 מקומות בשורה
            print()                                         # בסוף הדפסה של שחקן עוברים שורה להדפסת שחקן הבאה
    
    if num == 1:                                            # עם פונקציה נשארת עם ארך שהוגדר, אז מדפיסים רשימה שלמה  
        countSpaces(plist,num,a = 0 ,b = len(plist))        # קריא לפונקציה מקבלת ארכים ומדפיסה רשימה שלמה  
    elif num < 0:                                           # עם ארך שלילי - זה הוגדר בקריאת פונקציה כדי להדפיס שחקנים מסוף רשימה
        countSpaces(plist,num,a = len(plist)+num ,b = len(plist)) # value a = len(plist) + num - זה ארך שלילי בגלל זה יהיה פעולת חיסור מארך של אורך רשימה
    else:                                                   # אחרח זה עם להדפיס כמות מסוימת מהתחלה
        countSpaces(plist,num,a = 0 ,b = num)


# def sortPlayers(plist):                                   # מיון רשימה על ידי תכונה sort
#     plist = sorted(plist, key=lambda plist: plist[3],reverse=True)
#     return plist


def sortPlayers(plist):                                    # מיון ידני
    for i in range(len(plist)):
        for j in range(len(plist)-i-1):
            if plist[j][len(plist[i])-1] < plist[j+1][len(plist[i])-1]:
                plist[j], plist[j+1] = plist[j+1], plist[j]
    return plist                                            # מחזירה רשימה ממויינת



def addPlayer(plist):                                       # פונקציה הוספת שחקן חדש
    newplayer = []                                          # מיצרים רשימה חדשה בשביל פרטים של שחקן חדש
    while True:                                             # מפעילים לולאה אין סוף עד שתכונות הבאות לא יתבצעו בעזרת תכונת תפיסת טעויות     
        try:                                                
            newplayer.append(input('Enter name: '))         
            newplayer.append(input('Enter birthday[dd/mm/yyyy]: '))
            newplayer.append(int(input('Enter number of wins in tournaments: ')))
            newplayer.append(int(input('Enter number of points: ')))
            break                                           # עם כל אחד מפרטים נקלט לרשימה חדשה אז מפעילים BREAK
        except (ValueError) as error:                       # במקרא עם הכניסו משהוא שלא לפי סוג משתנה שהוגדר אז מופיה טעות ובקשת לרשום פרטים מהתחלה
            print(error)    
    return plist.append(newplayer)                          # מחזיר רשימה מחודשת עם שחקן חדש



def removePlayer(plist):                                    # פונקציה מחיקת שחקן
    sub = input('Enter name: ')                             # מחנישים שם או שם משפחה אפילו חלכי
    for i in range(len(plist)):                         # לולאת חיפוס מרשימה סאבסטרינג
        if sub.lower() in plist[i][0].lower():          # כולל רגיסטר עם יש ברשימה אותו שם והוא ראשון ברשימה
        # if plist[i][0].find(sub) != -1:               # לא כולל רגיסטר
            print(f'{plist[i][0]} was deleted')         # הודעה מתאימה
            plist.pop(i)                                # מוחקים אותו
            return plist                                # מחזירה רשימה חדשה בלי שחקן
    print('Not found')                                  # הודעה מתאימה עם לא מצאנו 
    return plist                                        # מחזיר רשימה איך שהיה



def Choose2Players(plist):                                          # פונקציה למשחק של 2 שחקנים בלבד


    def List2Players(plist,tournament_2players_plist, player):      # מיצרת רשימה של 2 שחקנים שישתתפו במשחק מקבלת רשימה ישנה, רשימה חדשה, ושם של שחקן
        for i in range(len(plist)):                                 # לולאה חיפוש ברשימה שם של שחקן
            if player.lower() in plist[i][0].lower():               # עם שחקן נמצא ברשימה כולל רגיסטר
                tournament_2players_plist.append(plist[i])          # מכניסים שחקן לרשימה חדשה
                print(f'"{plist[i][0]}" added')                     # הודעה מתאימה
                return tournament_2players_plist                    # מחזירה רשימה
        print(f'"{player}" not found')                              # הודעה מתאימה עם שחקן לא נמצא
        return tournament_2players_plist                            # מחזירה רשימה איך שהיא

    tournament_2players_plist = []                                  # רשימה חדשה לשתי שחקנים
    while True:                                                     # לולא אין סוף
        first_player = input('Enter name of first player: ')        # שם ראשון של שחקן שנבחר
        tournament_2players_plist = List2Players(plist,tournament_2players_plist, first_player) # רשימה משתנה לפי תוצאה בפונקציה
        if len(tournament_2players_plist) == 1:                     # במקרא עם רשימה מלאה אז עוצרים לולאה אין סוף
            break
    while True:                                                     # אותו דבר עם שחקן שני
        second_player = input('Enter name of second player: ')
        tournament_2players_plist = List2Players(plist,tournament_2players_plist, second_player)
        if len(tournament_2players_plist) == 2:
            break
    return tournament_2players_plist                                # פונקציה מחזירה רשימה עם שתי שחקנים



def doTournament(tname,plist,pamount,tournament_plist):             # פונקציה שמקבלת שם תחרות רשימת שחקנים כמות אקראי של משתתפים בתחרות בחיזקה 2 ורשימה שמקבלת שחקנים שנבחרו
    
    def choicePlayers(plist,pamount,tournament_plist):              # פונקציה שממלא רשימה חדשה 
        
        
        tournament_plist = random.sample(plist,pamount)             #  על ידי תכנו ברנדום מוציאים מרשימה ישנה כמות שחקנים בחיזקה 2 רנדומלים
        sleep(SLEEP_TIME)                                           # המתנה 
        return tournament_plist                                     # מחזירים רשימה חדשה עם שחקנים שנבחרו לתחרות

    tournament_plist = choicePlayers(plist,pamount,tournament_plist)    # רשימה חדשה מקבלת תוצאה מפונקציה
    print(f'Tournament: {random.choice(tournaments)[0]}')               # הדפסת שם תחרות רנדומלי
    sleep(SLEEP_TIME)                                                   #  המתנה
    print(f'Players: ',end='')                                          # הדפסת שחקנים שנבחרו
    for i in range(len(tournament_plist)):
        print(f'{tournament_plist[i][0]}',end=', ')                     # מדפיסים רק שמות
    print()
    return tournament_plist                                             # פונקציה מחזירה רשימה חדשה


def doSuperBowl(players):                                               # פונקציה של תחרות שחקנים מקבלת רשימה
    i = 0                                                               # אינדקס בשבילי לרוץ ברשימה של שחקנים שנבחרו לתחרות.
    # עם האנדקס אני מגדיר כל זוג שחקנים כמו "i and i+1"
    # כשה אחד מזוג שחקנים מפסיד אז אני מוחק אותו מרשימת שחקנים. ואז אחרי כל משחק אני מקטין רשימה ל-1 שחקן.
    # כל פעם אינדקס צריך לקדם לאחד שזוגות אתחדשו. אבל נגיד בתחרות של 8 שחקנים אחרי 4 משחקים אינדקס מגיע מ-0 ל-3 ואין לאן לקדם אותו
    # כי רשימה התצמצמה ל4שחקנים כבר. בגלל זה צריך להפס אינדקס כשה ארך שלו +1 יותר גדול מרשימה.
    # כשה אורך של רשימה הגיע לארך 1 אז זה אומר שנשאר רק שקחן אחד ברשימה והוא יש מנצח.
    # ומשם יצאים מלולא על ידי break
    
    while i <= len(players):                                             
        if i+1 > len(players):
            i = 0
        winner,players = doMatch(players,i)                                   # קריא לפונקציה  שמחזירה מנצח של כל זוג
        i += 1
        if len(players) == 1:
            break
    # print(f"{winner} tournament's winner")                            # הדפסה מתאימה
    return winner,players



def doMatch(players,i):                                               # מקבלת רשימהת שחקנים ואינדקס 
    p1winsets = p2winsets = 0                                         # משתנים  כמות נצחונות של כל שחקן בסאטים
    countsets = 1                                                     # מספור של סאטים בשביל הדפסה
    print(f'Match {players[i][0]} - {players[i+1][0]}')               # הדפסה של תחילת משחק בין 2 שחקניםשברשימה הם אחד אחרי שני
    while p1winsets != SETS and p2winsets != SETS:                    # לולאה עד שכמות נצחונות של אחד השחקנים לא יהיה שווה למשתנה קבוע
        #:עובדים הפוך AND OR  שמתי לב אפילו דרך דבאגר בדקתי שאופרטורים 
        
        p1,p2 = players[i][0],players[i+1][0]                         # קיצור להדפסת שמות של שחקנים
        p1scoregame = p2scoregame = 0                                 # כמות נקודות בכל משחק של סאט
        p1scoreset = p2scoreset = 0                                   # כמות נקודות של סאטים
        countgames = 0                                                # מיספר של משחק של סאט
        print(f'Set {countsets}')                                     # הדפסה מספר סאט
        countsets+=1                                                  # קידום ארך של סאט
        while p1scoreset < 6 and p2scoreset < 6:                      # לולאה עד שארך של נקודות בסאט לא יגיעה ל6
            countgames+=1                                             # מקדמים מספר משחק
            p1scoreset,p2scoreset = doSet(countgames,p1,p2,p1scoregame,p2scoregame,p1scoreset,p2scoreset,i) # קריה לפונקציה שמשחקת סאט ומחזירה ארכים של נקודות של סאט
        if p1scoreset > p2scoreset:                                   # כשה כמות נקודות הגיעה לשיש אז עם זה שחקן ראשון
            p1winsets += 1                                            # אז מעלים כמות נצחונות על פי סאט
            print(f'Set winner {p1}: {p1winsets}:{p2winsets}')        # הודעה מתאימה
        else:                                                         # אותו דבר עם שחקן שני
            p2winsets+=1
            print(f'Set winner {p2}: {p1winsets}:{p2winsets}')
    if p1winsets > p2winsets:                                         # אחרי ששחקו כמות סאטים לפי תנאים בדיקה מי מנצח.עם שחקו ראשון
        players[i][3] += 10                                           # מעלים כמות נקודות כמנצח במשחק
        players[i][2] += 1                                            # גם מעלים כמות נצחונות
        print(f'match winner: {p1} - {players[i][3]}')                # הודעה מתיאמה
        print(f'match loser: {players.pop(i+1)[0]}')                  # מחיקה של שחקן שהפסיד מרישה וגם הודעה מתאימה
        return p1,players                                             # פונקציה מחזירה רשימה רק עם מנצח ושם של מנצח
    else:    
        players[i+1][3] += 10                                         # אותו דבר לשחקן שני
        players[i+1][2] += 1
        print(f'match winner: {p2} - {players[i+1][3]}')
        print(f'match loser: {players.pop(i)[0]}')
        return p2,players

def doSet(countgames,p1,p2,p1scoregame,p2scoregame,p1scoreset,p2scoreset,i):  # פונקציה של משחק אחד של סאט
    print(f'game {countgames}',end=': ')                                      # game number
    while p1scoregame <= 40 and p2scoregame <= 40:                            # לולאה עד שאחד משחקנים לא יקבל 40 ניקודות

        p1scoregame,p2scoregame = doGame(p1scoregame,p2scoregame)             # קריה לפונקציה שמבצעת משחק אחד של סאט ומחזירה כמות ניקודות של כל שחקן

    if p1scoregame > 40:                                                      # עם שחקן ראשון זכה
        p1scoreset+=1                                                         # הוא מקבל נקודה בסאט
        print(f'game winner {p1}:\t{p1scoreset}:{p2scoreset}')                # הודעה מתאימה מנצח ו תוצאות של משחק
    else:                                                                     # אותו דבר ל שחקן שני
        p2scoreset+=1   
        print(f'game winner {p2}:\t{p1scoreset}:{p2scoreset}')
    return p1scoreset,p2scoreset                                              # פונקציה מחזירה ארכים של ניקוד בסאט
            

def doGame(p1scoregame,p2scoregame):                                          # פונקציה מבצעת משחק אחד עד 40 ניקודות
    p1random, p2random = random.randrange(0,1000),random.randrange(0,1000)    # מספרים אקראים של כל שחקן
    sleep(SLEEP_TIME)                                                       # המתנה לפי בקשה
    if p1random > p2random:                                                   # עם משפר ראשון יותר גדול משני
        p1scoregame += 10 if p1scoregame >= 30 else + 15                      # מוסיפים 15 ניקודות עם כמות ניקודות פחות מ30 אחרת 10 ניקודות
        if p1scoregame > 40:                                                  # עם כמות ניקודות יותר מ40
            return p1scoregame,p2scoregame                                    # פונקציה מחזירה ארכים של שחקנים
    else:                                                                     # אותו דבר לשחקן שני
        p2scoregame += 10 if p2scoregame >= 30 else + 15
        if p2scoregame > 40:
            return p1scoregame,p2scoregame 
    print(f'{p1scoregame}-{p2scoregame}',end=',')                             # הדפסת תוצאות
    return p1scoregame,p2scoregame                                            # מחזירה כמות ניקודות




def menu(tournaments,plist,pamount,tournament_plist):                         # תפרית
    while True:                                                               # לולאה אין סוף
        try:
            # sleep(2)
            print("1.Print all players")
            print("2.Print all sorted players")
            print("3.Print players from start list")
            print("4.Print players from end list")
            print("5.Add new player")
            print("6.Remove player")
            print("7.Tournament")
            print("0.Exit")
            choose = int(input('Make your chooise: '))
            if choose == 1:
                print('====================All not sorted====================')
                printPlayers(plist)                                                         # הדפסה לא ממויינת
            if choose == 2:
                print('====================All sorted====================')
                plist = sortPlayers(plist)                                                  # רשימה חוזרת ממויינת מפונקציה
                printPlayers(plist)                                                         # הדפסת רשימה
            if choose == 3:
                print('====================First====================')
                choosestartindex = int(input("Choose top players: "))                       # כמות אנשים להדפסה מהתחלה
                printPlayers(plist,choosestartindex)                                        # קריא לפונקציה ומעברים 2 פרמטרים
            if choose == 4:
                print('====================Last====================')
                chooseendindex = int(input("Choose count last players: "))
                printPlayers(plist,-chooseendindex)                                         # קריא לפונקציה ומעברים 2 פרמטרים אחד מהם שלילי! זה חשוב
            if choose == 5:
                print('====================Add new player====================')
                addPlayer(plist)                                                            # הוספת שחקן
            if choose == 6:
                print('====================Remove Player====================')
                printPlayers(plist)                                                         # הדפסה
                plist = removePlayer(plist)                                                 # רשימה חדשה עם שחקן שנמחק
                printPlayers(plist)                                                         # הדפסה של רשימה חדשה
            if choose == 7:
                while True:                                                                 # לולא אין סוף
                    try:
                        os.system('cls')                                                    # מרוקן את קונסול
                        print('1.Start tournament random')
                        print('2.Start tournament')
                        print('0.Exit')
                        sub_choose = int(input('Make your chooise: '))
                        # sleep(2)
                        if sub_choose == 1:
                            os.system('cls')
                            printPlayers(plist)
                            tournament_plist = doTournament(tournaments,plist,pamount,tournament_plist) # בניית רשימה חדשה אקראית של שחקנים שנבחרו לתחרות
                            if pamount > 2:                                                             # עם כמות שחקנים יותר מ זוג
                                winner,players = doSuperBowl(tournament_plist)                          # אז קודם קריה לפונקציה הזאת אם הגדרת אנדקסים 
                                players[0][3] += 10                                                     # מי שזכה בתחרות מקבל 10 ניקודות לניקודות ישיות
                                print(f"{winner} tournament's winner - {players[0][3]}")          
                            else:
                                winner,players = doMatch(tournament_plist,i=0)                          # אחרת זה אומר שתחרות של זוג וישר לפונקציה של משחק. פונקציה מחזירה רשימה של מנצח עם פרטים. ורק שם של מנצח
                                players[0][3] += 10                                                     # מי שזכה בתחרות מקבל 10 ניקודות לניקודות ישיות
                                print(f"{winner} tournament's winner - {players[0][3]}")                # הדפסת מנצח
                            break
                        if sub_choose == 2:                                                             
                            os.system('cls')
                            printPlayers(plist)                                                         # הדפסת רשימה
                            tournament_plist = Choose2Players(plist)                                    # קריא לפונקציה שמוציא 2 שחקנים לפי חיפוש על ידי סאבסטרינג ומחזירה רשימה עם שתי נבחרים
                            printPlayers(tournament_plist)                                              # הדפסת רשימה חדשה
                            sleep(2)                                                                    # המתנה
                            winner,players = doMatch(tournament_plist,i=0)                              # אותו דבר כמו לפני
                            players[0][3] += 10
                            print(f"{winner} tournament's winner - {players[0][3]}")
                            break
                        if sub_choose == 0:                                                             # יציא מהלולאה
                            break
                    except (ValueError) as error:                                                       # הדפסת טעויות עם סוג משתנה שונה ממה שהוגדר
                        print(error)
            if choose == 0:
                break
        except (ValueError) as error:
            print(error)



def main():                                                         # פונקציה ראשית
    menu(tournaments,players,pamount,tournament_plist)



if __name__ == "__main__":                                          
    main()                                                          # קריא לפונקציה ראשית

