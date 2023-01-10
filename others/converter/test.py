import mysql.connector
import xlrd
import xlsxwriter

cnx = mysql.connector.connect(host="localhost",user="root",passwd="",database="ats")
con = cnx.cursor()
    
sql = "SELECT * FROM cron_resume_extraction WHERE status='PENDING'"
con.execute(sql)
res = con.fetchall()
print(res)
    
    
file_loc = res[0][4]

file = xlrd.open_workbook(file_loc)
sheet = file.sheet_by_index(0)
                    
main_content = []
k = 0
for i in range(1,sheet.nrows):   
    cont = [] 
    isError = 0
    for j in range(6):
                      
        try :
            t = sheet.cell_value(i,j) // 1
            t = str(t).replace(".0","")
                               
        except :
            t = str(sheet.cell_value(i,j))
                        
                        
        if len(t) == 0 :
            cont.append("")
            isError = 1
        else :
            cont.append(t)
                            
    if isError == 1 :
        cont.append("NO")
    else :
        cont.append("YES")
                        
    main_content.append(cont)    
                    
print(main_content)  
                
    
con.close()