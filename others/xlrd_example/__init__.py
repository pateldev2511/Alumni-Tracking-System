from flask import Flask,render_template
import xlrd
from requests import get
import urllib.request, json
import requests
import cron
from cron import email_list
import mysql.connector

app = Flask(__name__)
app.secret_key = "1509"



@app.route('/',methods=['GET','POST'])
def index():
    colleges = ['Government College of Arts, Science and Commerce, Sanquelim - Goa. ','Government College of Arts, Science & Commerce, Khandola, Marcela – Goa.','Goa College of Home Science, Campal, Panaji – Goa.','Sant Sohirobanath Ambiye Government College of Arts & Commerce, Pernem – Goa.','Government College of Arts, Science and Commerce. Quepem - Goa.','Government College of Commerce, Borda,Margao – Goa.','Goa College of Music, Altinho, Panaji - Goa. ','Fr. Agnel College of Arts & Commerce, Pillar-Goa.','Goa University,Taleigao, Plateau-Goa.','S. S. Dempo College of Commerce & Economics, Altinho, Panaji-Goa.','Narayan Zantye College of commerce, Bicholim.','Dnyanprassarak Mandal’s College of Arts, Sou sheela Pramanand Vaidya College of  Science and VNS Bandekar College of Commerce, Bardez-Goa','DPM\'s Shree Mallikarjun College of Arts & Commerce, Delem-Canacona','V.M.Salgaocar College of Law Miramar-Panjim-Goa','S.V\'s Sridora Caculo College of Commerce & Management Studies, Khorlim, Mapusa Goa','G.R. Kare College of Law, Comba, Margao-Goa.','Nirmala Institute of Education, Altinho, Panaji-Goa','VVM\'s Shree Damodar College of Commerce and Economics, Margao – Goa','Dempo Charities Trust\'sDhempe College of Arts & Science, Miramar-Panaji-Goa','Parvatibai Chowgule College of Arts and Science,Margao Goa','Murgaon Education Society’s College of Arts & Commerce, Zuarinagar','G.V.M\'s Dr. Dada Vaidya College of Education , Ponda-Goa','Vidya Prabodhini College of Commerce, Education, Computer and Management – Vidya Nagar, Parvari – Goa ','Rosary College of Arts & Commerce, Navelim','Carmel College of Arts, Science and Commerce for Women, Nuvem','GVM College of Commerce & Economics, Farmagudi, Ponda-Goa.','Cuncolim Education Society’s   College of Arts & Commerce,Cuncolim-Goa.','St. Xavier\'s College of Arts, Science & Commerce,Mapusa-Goa.','P.E.S.s Shri Ravi Sitaram Naik College of Arts & Science, Farmagudi, Ponda-Goa.','P.E.S.\'s College of Education, Farmagudi, Ponda-Goa.','Shree Sateri Pissani Education Society\'s Shri Gopal Gaonkar Memorial College Goa Multi- Faculty College, Dayanandnagar, Dharbandora – Goa.','Swami Vivekanand Vidya Prasarak Mandal,Shirshire, Bori-Ponda','Adarsha Institute of ManagementFatorda-Goa.']
      
    x = [15.560024,15.521537,15.488579,15.702666,15.226190,15.285372,15.485113,15.439491,15.458777,15.470770,15.583293,15.595444,14.999852,15.482567,15.595407,15.274361,15.491437,15.274253,15.482454,15.289897,15.392232,15.407157,15.527069,15.255570,15.310893,15.406714,15.178994,15.598002,15.412738,15.401428,15.396453,15.365503,15.292304]
    
    y = [74.017567,73.957766,73.817067,73.819096,74.077318,73.974315,73.827175,73.893849,73.834300,73.861437,73.965412,73.797218,74.058952,73.811029,73.805108,73.951403,73.822935,73.952044,73.810310,73.980408,73.863927,73.993588,73.831187,73.965179,73.944982,73.992963,73.996707,73.808333,73.989280,74.012910,74.096119,74.021155,73.974188]
    
    
    return render_template('index.html',x=x,y=y,l=len(x),colleges=colleges)

@app.route('/readfile',methods=['GET','POST'])
def read_file():
    # try : 
    #     cnx = mysql.connector.connect(host='localhost',user='root',passwd='',database='cron_test')
    #     con = cnx.cursor()
    # except :
    #     print('Connection Error')
    #     pass
    
    ans = "<table border='1'>"
    file_loc = "D:/ALUMNI_TRACKING_SYSTEM/xlrd_example/COLLEGE_BULK_REGISTRATION_SHEET.xlsx"
    file = xlrd.open_workbook(file_loc)
    sheet = file.sheet_by_index(0)
    for i in range(sheet.nrows):
        ans += "<tr>"        
        for j in range(sheet.ncols):
            if i == 0 :
                ans += "<th style='padding:10px;'>"+str(sheet.cell_value(i,j))+"</th>"
            else :
                try :
                    t = sheet.cell_value(i,j) // 1
                    t = str(t).replace(".0","")
                    ans += "<td style='text-align:center;padding:10px;'>"+str(t)+"</td>"
                except :
                    ans += "<td style='text-align:center;padding:10px;'>"+str(sheet.cell_value(i,j))+"</td>"
                # try :
                #     sql = "INSERT INTO test(email,isSend) VALUES('%s','NO')" % (str(sheet.cell_value(i,j)))
                #     con.execute(sql)
                #     cnx.commit()
                # except :
                #     pass
        ans += "</tr>"
    ans += "</table>"
    # con.close()
    return ans


if __name__ == "__main__" :
    app.run(debug=True)