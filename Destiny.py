import random
import csv

class Destiny:
    
    __messages = []
    __money = []

    # 讀取 CSV 檔案
    def choice(self):
        with open('destiny.csv', newline='', encoding='utf-8') as csvfile:
            rows = csv.DictReader(csvfile)
            for row in rows:
                self.__messages.append(row['命運訊息'])
                self.__money.append(row['金額'])
            
        # 隨機抽取一張
        nums = random.randint(0,len(self.__messages)-1)
        return (self.__messages[nums],self.__money[nums])
    

if __name__ == "__main__":
    myDestiny = Destiny()
    print(myDestiny.choice())