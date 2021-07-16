class Messages:
    
    def inputData(self,messages):
        self.__messages = messages
        # 開啟檔案，設定成可寫入模式
        new_files = open("messages.txt","w", encoding='utf-8')

        # 將串列寫入檔案中
        new_files.writelines(messages)

        # 關閉檔案
        new_files.close()
    
    def outputData(self):
        files = open("messages.txt","r", encoding='utf-8')
        messages = []
        messages = files.readlines()
        self.__messages = messages[0]
        return self.__messages

if __name__ == "__main__":
    news = Messages()
    news.inputData("測試用")
    print(news.outputData())