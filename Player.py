import csv
class Player:
    # 初始化玩家，每人發 20000 遊戲幣以及出發位置為 0
    def __init__(self,money = 20000, po = 0):
        self.__money = money
        self.__po = po
        self.__status = 0

    # 設定玩家名稱
    def setName(self,name,id):
        self.__name = name
        self.__id = id
        with open('players.csv','a',newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([self.__id,self.__name,self.__money,self.__po,self.__status])

    # 取得玩家名稱
    def getName(self):
        return self.__name
        
    # 修改玩家遊戲幣
    def setMoney(self,money,id):
        self.__money += money
        table = [['id','name','money','po','status']]
        with open('players.csv','r',newline='') as csvfile:
            rows = csv.DictReader(csvfile)
            for row in rows:
                if (row.get('id') == str(id)):
                    row['money'] = str(int(row['money'])+money)
                table.append([row['id'],row['name'],row['money'],row['po'],row['status']])
        with open('players.csv','w',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(table)
        
    # 取得玩家遊戲幣
    def getMoney(self):
        return self.__money
        
    # 修改玩家位置
    def setPo(self,move):
        self.__po += move
        
    # 取得玩家位置
    def getPo(self):
        return self.__po

if __name__ == "__main__":
    myplayer = Player()
    myplayer.setMoney(1000,0)
