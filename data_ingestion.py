import sys
import sqlite3
import zipfile
import os
from datetime import datetime,timedelta
class BV_Process:
    def __init__(self):
        self.srcfiles_fldr='C:\\Users\\bvnku\\OneDrive\\Desktop\\Python\\Bazaarvoice\\srcfiles'
    def getfilename(self):
        prv_day=datetime.now()+timedelta(days = -2)
        self.filedate=prv_day.strftime("%d%m%Y")
        self.filename='bv_'+self.filedate+'.zip'
    def isfileexist(self):
        self.srcfilepath=self.srcfiles_fldr+ '\\' +self.filename
        if os.path.isfile(self.srcfilepath):
            print("{} file existed".format(self.srcfilepath))
        else:
            print("{} file is not existed".format(self.srcfilepath))
            self.stop()
    def filecountcheck(self):
        self.extracted_fldr=self.srcfiles_fldr+'\\'+'BV_'+self.filedate
        self.files_lst=os.listdir(self.extracted_fldr)
        if len(self.files_lst)==3:
            print("Matched")
        else:
            print("Mismatched")
            self.stop()
    def filerecordcountcheck(self):
        print(self.files_lst)
        for file in self.files_lst:
            filepath=os.path.join(self.extracted_fldr,file)
            f=open(filepath,"r")
            lines=f.readlines()
            file_lines_cnt=len(lines[1:-1])
            print(file,"file count=",file_lines_cnt)
            rec_cnt=lines[-1].split(',')[1]
            print(file,"record count=",rec_cnt)
            if file_lines_cnt==int(rec_cnt):
                print(file,"count matched")
            else:
                print(file,"count not matched")
                self.stop()
            f.close()
    def loaddataintotable(self):
            for file in self.files_lst:
                if file == 'reviews.csv':
                #filepath = self.srcfiles_fldr + '\\'+file
                    filepath = os.path.join(self.extracted_fldr,file)
                    #path = 'C:\\Users\\india\\Desktop\\FullStackDE\\Python\\Bazaarvoice\\srcfiles\\BV_12092024\\reviews.csv'
    
                    f = open(filepath, 'r')
                    lines = f.readlines()
                    records = lines[1:-1]
                    
                    for rec in records:
                        elements = rec.split(',')
                        print(elements)
                        reviewid = elements[0]
                        reviewtext = elements[1]
                        productid = elements[2].split('\n')[0]
                        qry = "insert into reviews_dtls values('{}','{}','{}')".format(reviewid,reviewtext,productid)
                        print(qry)
                        conn = sqlite3.connect('C:\\Users\\bvnku\\OneDrive\\Desktop\\devpractise.db')
                        curr = conn.cursor()
                        res = curr.execute(qry)
                        conn.commit()
                        curr.close()
                        conn.close()
                        
        
        
    def unzipfile(self):
        with zipfile.ZipFile(self.srcfilepath,"r") as zip_ref:
            zip_ref.extractall(self.srcfiles_fldr)

    def stop(self):
        sys.exit()
        
if __name__=="__main__":
    bv=BV_Process()
    bv.getfilename()
    bv.isfileexist()
    bv.unzipfile()
    bv.filecountcheck()
    bv.filerecordcountcheck()
    bv.loaddataintotable()
