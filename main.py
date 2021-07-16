##############################
# Project: 大富翁遊戲主程式   #
# Version: 0.1               #
# Date: 2021/07/16           #
# Author: Antallen           #
# Content: 使用 Player 物件
##############################

# 引用 random 類別中的 randrange() 函數
from random import randrange

# 引用 Player 物件
import Player

# 引用 Chance 物件
import Chance
import Destiny
# 引用 Stores 物件
import Stores

# 引用 playMap 物件
import playMap

import Messages

# 常用函式、參數設定區域
## 遊戲方格總數
areas = 24

## 處理玩家是否有經過「開始」
def playerPo(steps):
    if (steps >= areas):
        nums = (steps % areas)
        return nums
    else:
        return steps

## 清除舊資料
def clearOldData():
    files = open('players.csv','w',encoding='utf-8')
    files.truncate()
    titles = "id,name,money,po,status\n"
    files.writelines(titles)
    files.close()
    files = open('messages.txt','w',encoding='utf-8')
    files.truncate()
    titles = "遊戲即將開始...."
    files.writelines(titles)
    files.close()

# 程式流程開始
# 使用 if __name__
if __name__ == "__main__":

    # 要求玩家要輸入遊戲人數
    players_num = eval(input("請輸入玩家人數："))

    # 建立玩家物件
    players = []

    # 按照遊戲人數，使用 Player 類別
    # 逐次產生玩家名稱、玩家代號、玩家初始遊戲幣、玩家初始位置等物件內容
    clearOldData()
    for i in range(players_num):
        players.append(Player.Player())
        # 要求玩家輸入玩家名稱
        players[i].setName(input("請輸入玩家名稱:"),i)
        
    # 設定玩家位置值
    players_po = []
    for i in range(players_num):
        players_po.append('0')
    
    # 設定玩家順序值
    i = 0
    myMap = playMap.playMap()
    
    # 設定訊息存放物件
    news = Messages.Messages()
    news.inputData("請按下《ＥＮＴＥＲ》進行遊戲")
    myMap.printMap(players_po)
    input()
    
    # 開始進行遊戲
    while True:
        #### 判斷玩家資格
        ##### 計算可遊戲玩家
        new_players_num = 0
        for num in range(len(players)):
            if (players[num].getStatus() != -1):
                new_players_num = new_players_num + 1
        players_num = new_players_num
        if (players_num == 1):
            news.inputData("只剩下一位玩家！遊戲結束！")
            myMap.printMap(players_po)
            break
        if (players[i].getStatus() == -1):
            news.inputData(myMap.transferNo(str(i+1)) + "號玩家己破產《ＥＮＴＥＲ》")
            myMap.printMap(players_po)
            input()
            i = i + 1
            if (i >= players_num):
                i = i - players_num
            continue
        elif (players[i].getStatus() > 0):
            newstatus = players[i].getStatus() - 1
            players[i].setStatus(-1)
            news.inputData(myMap.transferNo(str(i+1)) + "號玩家休息" + myMap.transferNo(str(newstatus)) + "次")
            myMap.printMap(players_po)
            input()
            i = i + 1
            if (i >= players_num):
                i = i - players_num
            continue
    ##### a.) 印出地圖
        news.inputData(myMap.transferNo(str(i+1)) + "號玩家按下《ＥＮＴＥＲ》進行遊戲")
        myMap.printMap(players_po)
        input()
    ##### b.) 擲骰子
        oldpo = players[i].getPo()
        newstep = randrange(1,6)
        news.inputData(myMap.transferNo(str(i+1)) + "號玩家擲骰子：" + myMap.transferNo(str(newstep)) + "點")
        myMap.printMap(players_po) # 印地圖
        # 設定玩家新的位置
        players[i].setPo(newstep)
    ##### c.) 移動到骰子點數的框格
        newpo = players[i].getPo()
        
        #　I. 可能經過起點
        if ((int(newpo/areas) > int(oldpo/areas)) and ((newpo % areas) != 0)):
            news.inputData(myMap.transferNo(str(i+1)) + "號玩家越過「開始」位置《ＥＮＴＥＲ》")
            players[i].setMoney(2000,i)
            myMap.printMap(players_po)
            input()
            news.inputData(myMap.transferNo(str(i+1)) + "號玩家得２０００《ＥＮＴＥＲ》")

        newpo = playerPo(newpo)
        players_po[i] = str(newpo)
        myMap.printMap(players_po)
        input()
        news.inputData(myMap.transferNo(str(i+1)) + "號玩家在新位置：" + myMap.transferNo(str(newpo)) + "《ＥＮＴＥＲ》")
        myMap.printMap(players_po)
        input()
        #  II. 可能落在邊角框格
        if (newpo == 0):
            news.inputData(myMap.transferNo(str(i+1)) + "號玩家回到「開始」位置《ＥＮＴＥＲ》")
            myMap.printMap(players_po)
            input()
        elif (newpo  == 6):
            #print(" 休息一天")
            news.inputData(myMap.transferNo(str(i+1)) + "號玩家，無事休息一天《ＥＮＴＥＲ》")
            myMap.printMap(players_po)
            input()
        elif (newpo  == 18):
            #print(" 再玩一次")
            news.inputData(myMap.transferNo(str(i+1)) + "號玩家，再玩一次《ＥＮＴＥＲ》")
            myMap.printMap(players_po)
            input()
            continue
        elif (newpo == 12):
            players[i].setStatus(3)
            news.inputData(myMap.transferNo(str(i+1)) + "號玩家，休息三次《ＥＮＴＥＲ》")
            myMap.printMap(players_po)
            input()
        #  III. 可能是在機會與命運框格
        ## 機會的地圖編號是 3,15 兩個號碼
        elif ((newpo == 3) or (newpo == 15)):
            myChance = Chance.Chance()
            chances = myChance.choice()
            news.inputData(myMap.transferNo(str(i+1)) + "號玩家中機會：" + chances[0])
            players[i].setMoney(int(chances[1]),i)
            myMap.printMap(players_po)
            input()
        ## 命運的地圖編號是 9,21 兩個號碼    
        elif ((newpo == 9) or (newpo == 21)):
            myDestiny = Destiny.Destiny()
            destines = myDestiny.choice()
            news.inputData(myMap.transferNo(str(i+1)) + "號玩家中命運：" + destines[0])
            players[i].setMoney(int(destines[1]),i)
            myMap.printMap(players_po)
            input()

        #  IV. 可能是在地產框格
        else:
            playerStore = Stores.Stores()
            store = playerStore.getStoreData(str(newpo))
            ## 判斷是否有人己取得該地產所有權了
            if store[2] == '-1':
                # 判斷是否可以買進，才進行遊戲
                if ((int(players[i].getMoney())-int(store[3])) >= 0):
                    news.inputData("該地產無人所有！是否買進？（Ｙ｜Ｎ）")
                    myMap.printMap(players_po)
                    results = input()
                    if ((results == 'Y') or (results == 'y')):
                        store[2] = str(i+1)
                        playerStore.setStoreData(store)
                        players[i].setMoney(0-int(store[3]),i)
                        news.inputData(myMap.transferNo(str(i+1)) + "號玩家買進地產：" + store[1])
                        myMap.printMap(players_po)
                        input()
                    else:
                        news.inputData(myMap.transferNo(str(i+1)) + "號玩家放棄買進")
                        myMap.printMap(players_po)
                        input()
                else:
                    news.inputData(myMap.transferNo(str(i+1)) + "號玩家資金不足，放棄買進")
                    myMap.printMap(players_po)
                    input()
            else:
                #print("該地產為：" + str(players[int(store[2])-1].getName()) + "所有")
                news.inputData("該地產為：" + store[2] + "號玩家所有")
                myMap.printMap(players_po)
                input()
                if ((int(store[2])-1) != i):
                    news.inputData("需支付：" + myMap.transferNo(store[3]))
                    myMap.printMap(players_po)
                    input()
                    # 需付費玩家
                    players[i].setMoney(0-int(store[3]),i)
                    if (players[i].getStatus() == -1):
                        players_num = players_num - 1
                    # 收費玩家
                    players[int(store[2])-1].setMoney(int(store[3]),int(store[2])-1)
                    myMap.printMap(players_po)
                    input()
                else:
                    news.inputData("不需支付費用給自已")
                    myMap.printMap(players_po)
                    input()

            playerStore = None
    ##### e.)
        # 輪至下一位玩家
        i = i + 1
        if (i >= players_num):
            i = i - players_num
    ##### f.) 結束遊戲條件
        if (i == 0):
            news.inputData("是否結束遊戲？Ｙ：是　其它：繼續")
            myMap.printMap(players_po)
            ends = input()
            if ((ends == "Y") or (ends == "y")):
                break