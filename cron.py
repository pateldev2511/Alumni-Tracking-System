from flask import Flask,render_template,json,jsonify
from flask_mail import Mail,Message
from requests import get
import urllib.request, json
import requests
import schedule
import time
import mysql.connector
from datetime import datetime
import yagmail
import json

import convertapi
import xlrd
import xlsxwriter 
import os

app_base_url = "http://127.0.0.1:5000/"

app = Flask(__name__)
app.secret_key = "1509"

mail=Mail(app)

UPLOAD_FOLDER = '/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'alumni.association.goa@gmail.com'
app.config['MAIL_PASSWORD'] = 'ats12345'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

def association_cron_for_alumni_email():
    association_cron_for_alumni_email_jobs_details = []
    cnx = mysql.connector.connect(host="localhost",user="root",passwd="",database="ats")
    con = cnx.cursor()
    try : 
        sql = "SELECT * FROM association_cron_details WHERE type='EMAIL'"
        con.execute(sql)
        res = con.fetchall()
        for i in res :
            association_cron_for_alumni_email_jobs_details.append([i[0],i[2],i[4],i[5]])
        # print("association_cron_for_alumni_job_details")
        # print(association_cron_for_alumni_email_jobs_details)
    except :
        print("Error In Getting association_cron_for_alumni_job_details")
        pass
    
    if len(association_cron_for_alumni_email_jobs_details) != 0 :
        for k in association_cron_for_alumni_email_jobs_details :
            # print(k)
            db_table_name = str(k[1])
            job_id = k[0]
            email_subject = str(k[2])
            email_content = str(k[3])
            # print("\ndb : ",db_table_name)
            sql = "SELECT * FROM "+str(db_table_name)+" WHERE isEmailSent='NO'"
            con.execute(sql)
            res = con.fetchall()
            for m in res :
                email = str(m[2])
                id_ = int(m[0])
                
                print("\nTrying To Send Mail To "+email+" From "+str(db_table_name))
                
                yag_smtp_connection = yagmail.SMTP( {"alumni.association.goa@gmail.com" : "Alumni Association Of Goa"}, password="ats12345", host='smtp.gmail.com',port=465)

    
                
        
                # email content with attached file path.
                
                html_con = '''
                <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title></title>
        </head>
        <body>
            <table class="nl-container" style="table-layout: fixed; vertical-align: top; min-width: 320px; margin: 0 auto; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #f5f5f5; width: 100%;" role="presentation" width="100%" cellspacing="0" cellpadding="0" bgcolor="#F5F5F5">
                <tbody>
                <tr style="vertical-align: top;" valign="top">
                    <td style="word-break: break-word; vertical-align: top;" valign="top">
                        <div style="background-color: transparent;">
                            <div class="block-grid" style="margin: 0 auto; min-width: 320px; max-width: 650px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: transparent;">
                            <div style="border-collapse: collapse; display: table; width: 100%; background-color: transparent;">
                                <div class="col num12" style="min-width: 320px; max-width: 650px; display: table-cell; vertical-align: top; width: 650px;">
                                    <div style="width: 100% !important;">
                                        <div style="border: 0px solid transparent; padding: 5px 0px 5px 0px;">
                                        <table class="divider" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
                                            <tbody>
                                                <tr style="vertical-align: top;" valign="top">
                                                    <td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding: 10px;" valign="top">
                                                    <table class="divider_content" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 0px solid transparent; height: 10px; width: 100%;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0" align="center">
                                                        <tbody>
                                                            <tr style="vertical-align: top;" valign="top">
                                                                <td style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top" height="10">&nbsp;</td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        <div style="background-color: transparent;">
                            <div class="block-grid two-up no-stack" style="margin: 0 auto; min-width: 320px; max-width: 650px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: #ffffff;">
                            <div style="border-collapse: collapse; display: table; width: 100%; background-color: #ffffff;">
                                <div class="col num6" style="min-width: 320px; max-width: 325px; display: table-cell; vertical-align: top; width: 325px;">
                                    <div style="width: 100% !important;">
                                        <div style="border: 0px solid transparent; padding: 25px 0px 25px 25px;">
                                        <div class="img-container left fixedwidth" style="padding-right: 0px; padding-left: 0px;" align="left">
                                            <img class="left fixedwidth" style="text-decoration: none; -ms-interpolation-mode: bicubic; border: 0; height: auto; width: 100%; max-width: 195px; display: block;" title="Image" src="http://cdn.mcauto-images-production.sendgrid.net/92f4cab4130b7228/6ac70d4b-6462-4a67-ac30-faec499c6d4f/256x105.png" alt="Image" width="195" border="0" /> 
                                        </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="col num6" style="min-width: 320px; max-width: 325px; display: table-cell; vertical-align: top; width: 325px;">
                                    <div style="width: 100% !important;">
                                        <div style="border: 0px solid transparent; padding: 25px 25px 25px 0px;">
                                        <div class="button-container" style="padding: 10px 0px 10px 10px;" align="right">
                                        </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        <div style="background-color: transparent;">
                            <div class="block-grid" style="margin: 0 auto; min-width: 320px; max-width: 650px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: #d6e7f0;">
                            <div style="border-collapse: collapse; display: table; width: 100%; background-color: #d6e7f0;">
                                <div class="col num12" style="min-width: 320px; max-width: 650px; display: table-cell; vertical-align: top; width: 650px;background-color:white;padding:20px">
                                    <div style="width: 100% !important;background-color:white;">
                '''
                
                html_con += str(email_content)
                
                html_con += '''
                <div style="background-color: white; border: 0px solid transparent; padding: 5px 25px 60px 25px;">
     
                               </div>
                             </div>
                          </div>
                       </div>
                    </div>
                 </div>
                 <div style="background-color: transparent;">
                    <div class="block-grid" style="margin: 0 auto; min-width: 320px; max-width: 650px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: transparent;">
                       <div style="border-collapse: collapse; display: table; width: 100%; background-color: transparent;">
                          <div class="col num12" style="min-width: 320px; max-width: 650px; display: table-cell; vertical-align: top; width: 650px;">
                             <div style="width: 100% !important;">
                                <div style="border: 0px solid transparent; padding: 20px 0px 60px 0px;">
                                   <table class="social_icons" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" role="presentation" width="100%" cellspacing="0" cellpadding="0">
                                      <tbody>
                                         <tr style="vertical-align: top;" valign="top">
                                            <td style="word-break: break-word; vertical-align: top; padding: 10px;" valign="top">
                                               <table class="social_table" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-tspace: 0; mso-table-rspace: 0; mso-table-bspace: 0; mso-table-lspace: 0;" role="presentation" cellspacing="0" cellpadding="0" align="center">
                                                  <tbody>
                                                     <tr style="vertical-align: top; display: inline-block; text-align: center;" align="center" valign="top">
                                                        <td style="word-break: break-word; vertical-align: top; padding-bottom: 5px; padding-right: 8px; padding-left: 8px;" valign="top"><a href="https://www.facebook.com/darshpatelofficial" target="_blank" rel="noopener"><img style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: none; display: block;" title="Facebook" src="http://cdn.mcauto-images-production.sendgrid.net/92f4cab4130b7228/93ef56de-a14b-43c0-8cda-7ba7f3b69b19/64x64.png" alt="Facebook" width="32" height="32" /></a></td>
                                                        <td style="word-break: break-word; vertical-align: top; padding-bottom: 5px; padding-right: 8px; padding-left: 8px;" valign="top"><a href="https://twitter.com/pateldarsh10" target="_blank" rel="noopener"><img style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: none; display: block;" title="Twitter" src="http://cdn.mcauto-images-production.sendgrid.net/92f4cab4130b7228/81c04100-cf31-4016-8820-9bf9296d39a0/64x64.png" alt="Twitter" width="32" height="32" /></a></td>
                                                        <td style="word-break: break-word; vertical-align: top; padding-bottom: 5px; padding-right: 8px; padding-left: 8px;" valign="top"><a href="https://instagram.com/pateldarsh_007" target="_blank" rel="noopener"><img style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: none; display: block;" title="Instagram" src="http://cdn.mcauto-images-production.sendgrid.net/92f4cab4130b7228/858aeae3-142f-4b84-8400-87cc7e0e92d8/64x64.png" alt="Instagram" width="32" height="32" /></a></td>
                                                        <td style="word-break: break-word; vertical-align: top; padding-bottom: 5px; padding-right: 8px; padding-left: 8px;" valign="top"><a href="mailto:mailto:alumni.association.goa@gmail.com" target="_blank" rel="noopener"><img style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: none; display: block;" title="E-Mail" src="http://cdn.mcauto-images-production.sendgrid.net/92f4cab4130b7228/89016f33-3bcf-4dc9-b8ee-a4b5bc249ea4/64x64.png" alt="E-Mail" width="32" height="32" /></a></td>
                                                     </tr>
                                                  </tbody>
                                               </table>
                                            </td>
                                         </tr>
                                      </tbody>
                                   </table>
                                   <div style="color: #555555; font-family: Lato, Tahoma, Verdana, Segoe, sans-serif; line-height: 1.5; padding: 10px;">
                                      <div style="font-size: 12px; line-height: 1.5; color: #555555; font-family: Lato, Tahoma, Verdana, Segoe, sans-serif; mso-line-height-alt: 18px;">
                                         <p style="font-size: 14px; line-height: 1.5; text-align: center; word-break: break-word; mso-line-height-alt: 21px; margin: 0;">&copy; 2020 - Alumni Association Of Goa - All Rights Reserved.</p>
                                      </div>
                                   </div>
                                </div>
                             </div>
                          </div>
                       </div>
                    </div>
                 </div>
              </td>
           </tr>
        </tbody>
     </table>
</body>
</html>
                '''
                
                
                
                msg = Message(email_subject, sender = ('Alumni Association Of Goa','alumni.association.goa@gmail.com'), recipients = [email])
                msg.html = html_con
                mail_sent = 0
                try :
                    mail.send(msg)
                    mail_sent = 1
                except :
                    print("Unable To Send Mail "+str(email)+" From "+str(db_table_name))
                if mail_sent == 1:
                    try :
                        sql = "UPDATE "+str(db_table_name)+" SET isEmailSent='YES' WHERE id=%d" % (id_)
                        con.execute(sql)
                        cnx.commit()
                        print("Mail Sent To "+str(email)+" With YES From "+str(db_table_name))
                    except:
                        print("Mail Sent To "+str(email)+" With NO From "+str(db_table_name))
                        pass
                else :
                    print("Unable To Send Mail "+str(email)+" From "+str(db_table_name))
                    
                try :
                    total_alumni_email = 0
                    sql = "SELECT * FROM "+str(db_table_name)+" WHERE membership_type='ALUMNI'"
                    con.execute(sql)
                    res = con.fetchall()
                    total_alumni_email = len(res)
                    
                    total_sent_alumni_email = 0
                    sql = "SELECT * FROM "+str(db_table_name)+" WHERE membership_type='ALUMNI' AND isEmailSent='YES'"
                    con.execute(sql)
                    res = con.fetchall()
                    total_sent_alumni_email = len(res)
                    
                    if total_alumni_email == total_sent_alumni_email :
                        sql = "UPDATE association_cron_details SET status_send_not_alumni='SENT' WHERE job_id=%d" % (job_id)
                        con.execute(sql)
                        cnx.commit()
                        print("\nUpdated Status Of send_not_alumni TO SENT on "+str(db_table_name))
                    else :
                        pass
                    
                except :
                    print("Error In Updating Association_cron_details For Alumni")
                 
                try :
                    total_college_email = 0
                    sql = "SELECT * FROM "+str(db_table_name)+" WHERE membership_type='COLLEGE_SPOC'"
                    con.execute(sql)
                    res = con.fetchall()
                    total_college_email = len(res)
                    
                    total_sent_college_email = 0
                    sql = "SELECT * FROM "+str(db_table_name)+" WHERE membership_type='COLLEGE_SPOC' AND isEmailSent='YES'"
                    con.execute(sql)
                    res = con.fetchall()
                    total_sent_college_email = len(res)
                    
                    if total_college_email == total_sent_college_email :
                        sql = "UPDATE association_cron_details SET status_send_not_colleges='SENT' WHERE job_id=%d" % (job_id)
                        con.execute(sql)
                        cnx.commit()
                        print("\nUpdated Status Of send_not_colleges TO SENT on "+str(db_table_name))
                    else :
                        pass
                    
                except :
                    print("Error In Updating Association_cron_details For Colleges")
                    
                
                try :
                    total_association_email = 0
                    sql = "SELECT * FROM "+str(db_table_name)+" WHERE membership_type='ASSOCIATION_MEMBER'"
                    con.execute(sql)
                    res = con.fetchall()
                    total_association_email = len(res)
                    
                    total_sent_association_email = 0
                    sql = "SELECT * FROM "+str(db_table_name)+" WHERE membership_type='ASSOCIATION_MEMBER' AND isEmailSent='YES'"
                    con.execute(sql)
                    res = con.fetchall()
                    total_sent_association_email = len(res)
                    
                    if total_association_email == total_sent_association_email :
                        sql = "UPDATE association_cron_details SET status_send_not_association='SENT' WHERE job_id=%d" % (job_id)
                        con.execute(sql)
                        cnx.commit()
                        print("\nUpdated Status Of send_not_association TO SENT on "+str(db_table_name))
                    else :
                        pass
                    
                except :
                    print("Error In Updating Association_cron_details For Association")
                        
                        
                    
                
    
    else :
        print("\nNo association_cron_for_alumni_job_details found.")
        
    con.close()
    

def association_cron_for_alumni_sms():
    association_cron_for_alumni_sms_jobs_details = []
    cnx = mysql.connector.connect(host="localhost",user="root",passwd="",database="ats")
    con = cnx.cursor()
    try : 
        sql = "SELECT * FROM association_cron_details WHERE type='SMS'"
        con.execute(sql)
        res = con.fetchall()
        for i in res :
            association_cron_for_alumni_sms_jobs_details.append([i[0],i[2],i[4],i[5]])
        # print("association_cron_for_alumni_job_details")
        # print(association_cron_for_alumni_email_jobs_details)
    except :
        print("Error In Getting association_cron_for_alumni_job_details")
        pass
    
    if len(association_cron_for_alumni_sms_jobs_details) != 0 :
        for k in association_cron_for_alumni_sms_jobs_details :
            # print(k)
            db_table_name = str(k[1])
            job_id = k[0]
            sms_title = str(k[2])
            sms_content= str(k[3])
            # print("\ndb : ",db_table_name)
            sql = "SELECT * FROM "+str(db_table_name)+" WHERE isSMSSent='NO'"
            con.execute(sql)
            res = con.fetchall()
            for m in res :
                mobile_no = "+"+str(m[2])
                id_ = int(m[0])
                
                print("\nTrying To Send SMS To "+mobile_no+" From "+str(db_table_name))
                
                
                headers = {
      'Content-Type': 'application/json',
      'APIKey': '5Amyg5TSwh3D11EY6GWtJ4SB8nAiav9Q'
  }
                sms_sent = 0
                f = open("temp_msg.txt",'w')
                f.write(sms_content)
                f.close()

                f = open("temp_msg.txt",'r')
                lines = f.readlines()

                msg = ""

                for line in lines :
                    line = line.strip()
                    if len(line) == 0 :
                            msg += "\\n"
                    else :
                            msg += line.strip()
                    
                f.close()
                # print(msg)
                data = '{"message": "'+msg+'","binary": false,  "destinations": ["'+mobile_no+'"]}'
                try :
                    response = requests.post('https://sandbox.api.sap.com/proximusenco/sms/outboundmessages', headers=headers, data=data)
                    resx = json.loads(response.text)
                    # print(resx)
                    # print(response.text)
                    if resx["deliveryInfo"][0]["deliveryStatus"] == "DeliveredToNetwork" :
                        sms_sent = 1
                    else :
                        sms_sent = 0
                except :
                    sms_sent = 0
                    print("Unable To Send SMS "+str(mobile_no)+" From "+str(db_table_name))
                
                
                if sms_sent == 1:
                    try :
                        sql = "UPDATE "+str(db_table_name)+" SET isSMSSent='YES' WHERE id=%d" % (id_)
                        con.execute(sql)
                        cnx.commit()
                        print("SMS Sent To "+str(mobile_no)+" With YES From "+str(db_table_name))
                    except:
                        print("SMS Sent To "+str(mobile_no)+" With NO From "+str(db_table_name))
                        pass
                else :
                    print("Unable To Send SMS "+str(mobile_no)+" From "+str(db_table_name))
                    
                try :
                    total_alumni_numbers = 0
                    sql = "SELECT * FROM "+str(db_table_name)+" WHERE membership_type='ALUMNI'"
                    con.execute(sql)
                    res = con.fetchall()
                    total_alumni_numbers = len(res)
                    
                    total_sent_alumni_numbers = 0
                    sql = "SELECT * FROM "+str(db_table_name)+" WHERE membership_type='ALUMNI' AND isSMSSent='YES'"
                    con.execute(sql)
                    res = con.fetchall()
                    total_sent_alumni_numbers = len(res)
                    
                    if total_alumni_numbers == total_sent_alumni_numbers :
                        sql = "UPDATE association_cron_details SET status_send_not_alumni='SENT' WHERE job_id=%d" % (job_id)
                        con.execute(sql)
                        cnx.commit()
                        print("\nUpdated Status Of send_not_alumni TO SENT on "+str(db_table_name))
                    else :
                        pass
                    
                except :
                    print("Error In Updating Association_cron_details For Alumni")
                 
                try :
                    total_college_numbers = 0
                    sql = "SELECT * FROM "+str(db_table_name)+" WHERE membership_type='COLLEGE_SPOC'"
                    con.execute(sql)
                    res = con.fetchall()
                    total_college_numbers = len(res)
                    
                    total_sent_college_numbers = 0
                    sql = "SELECT * FROM "+str(db_table_name)+" WHERE membership_type='COLLEGE_SPOC' AND isSMSSent='YES'"
                    con.execute(sql)
                    res = con.fetchall()
                    total_sent_college_numbers = len(res)
                    
                    if total_college_numbers == total_sent_college_numbers :
                        sql = "UPDATE association_cron_details SET status_send_not_colleges='SENT' WHERE job_id=%d" % (job_id)
                        con.execute(sql)
                        cnx.commit()
                        print("\nUpdated Status Of send_not_colleges TO SENT on "+str(db_table_name))
                    else :
                        pass
                    
                except :
                    print("SMS : Error In Updating Association_cron_details For Colleges")
                    
                
                try :
                    total_association_numbers = 0
                    sql = "SELECT * FROM "+str(db_table_name)+" WHERE membership_type='ASSOCIATION_MEMBER'"
                    con.execute(sql)
                    res = con.fetchall()
                    total_association_numbers = len(res)
                    
                    total_sent_association_numbers = 0
                    sql = "SELECT * FROM "+str(db_table_name)+" WHERE membership_type='ASSOCIATION_MEMBER' AND isSMSSent='YES'"
                    con.execute(sql)
                    res = con.fetchall()
                    total_sent_association_numbers = len(res)
                    
                    if total_association_numbers == total_sent_association_numbers :
                        sql = "UPDATE association_cron_details SET status_send_not_association='SENT' WHERE job_id=%d" % (job_id)
                        con.execute(sql)
                        cnx.commit()
                        print("\nUpdated Status Of send_not_association TO SENT on "+str(db_table_name))
                    else :
                        pass
                    
                except :
                    print("SMS : Error In Updating Association_cron_details For Association")
                        
                        
                    
                
    
    else :
        print("\nSMS : No association_cron_for_alumni_job_details found.")
        
    con.close()


# This is For Bulk Alumni Upload CRON
def college_bulk_registration():
    alumni_details = []
    cnx = mysql.connector.connect(host="localhost",user="root",passwd="",database="ats")
    con = cnx.cursor()
    res = []
    try :
        sql = "SELECT * FROM students_added_by_college WHERE isEmailSent='NO'"
        con.execute(sql)
        res = con.fetchall()
        # print(res)
    except :
        print("College : Error In Getting students_added_by_college List.")
    print("\n=====     BULK ALUMNI REGISTRATION     =====\n")   
    for i in res :
        mail_sent = 0
        user_id = int(i[0])
        verification_code = str(i[16])
        email = str(i[4])
        msg = Message('INVITATION TO JOIN ALUMNI ASSOCIATION OF GOA', sender = ('Alumni Association Of Goa','alumni.association.goa@gmail.com'), recipients = [email])
        msg.html = '''
                                                              <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml">

<head>
    <!--[if gte mso 9]><xml><o:OfficeDocumentSettings><o:AllowPNG/><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml><![endif]-->
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
    <meta content="width=device-width" name="viewport" />
    <!--[if !mso]><!-->
    <meta content="IE=edge" http-equiv="X-UA-Compatible" />
    <!--<![endif]-->
    <title></title>
    <!--[if !mso]><!-->
    <link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet" type="text/css" />
    <!--<![endif]-->
    <style type="text/css">
        body {
            margin: 0;
            padding: 0;
        }
        
        table,
        td,
        tr {
            vertical-align: top;
            border-collapse: collapse;
        }
        
        * {
            line-height: inherit;
        }
        
        a[x-apple-data-detectors=true] {
            color: inherit !important;
            text-decoration: none !important;
        }
    </style>
    <style id="media-query" type="text/css">
        @media (max-width: 670px) {
            .block-grid,
            .col {
                min-width: 320px !important;
                max-width: 100% !important;
                display: block !important;
            }
            .block-grid {
                width: 100% !important;
            }
            .col {
                width: 100% !important;
            }
            .col>div {
                margin: 0 auto;
            }
            img.fullwidth,
            img.fullwidthOnMobile {
                max-width: 100% !important;
            }
            .no-stack .col {
                min-width: 0 !important;
                display: table-cell !important;
            }
            .no-stack.two-up .col {
                width: 50% !important;
            }
            .no-stack .col.num4 {
                width: 33% !important;
            }
            .no-stack .col.num8 {
                width: 66% !important;
            }
            .no-stack .col.num4 {
                width: 33% !important;
            }
            .no-stack .col.num3 {
                width: 25% !important;
            }
            .no-stack .col.num6 {
                width: 50% !important;
            }
            .no-stack .col.num9 {
                width: 75% !important;
            }
            .video-block {
                max-width: none !important;
            }
            .mobile_hide {
                min-height: 0px;
                max-height: 0px;
                max-width: 0px;
                display: none;
                overflow: hidden;
                font-size: 0px;
            }
            .desktop_hide {
                display: block !important;
                max-height: none !important;
            }
        }
    </style>
</head>

<body class="clean-body" style="margin: 0; padding: 0; -webkit-text-size-adjust: 100%; background-color: #F5F5F5;">
    <!--[if IE]><div class="ie-browser"><![endif]-->
    <table bgcolor="#F5F5F5" cellpadding="0" cellspacing="0" class="nl-container" role="presentation" style="table-layout: fixed; vertical-align: top; min-width: 320px; Margin: 0 auto; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #F5F5F5; width: 100%;" valign="top" width="100%">
        <tbody>
            <tr style="vertical-align: top;" valign="top">
                <td style="word-break: break-word; vertical-align: top;" valign="top">
                    <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color:#F5F5F5"><![endif]-->
                    <div style="background-color:transparent;">
                        <div class="block-grid" style="Margin: 0 auto; min-width: 320px; max-width: 650px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: transparent;">
                            <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">
                                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:650px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
                                <!--[if (mso)|(IE)]><td align="center" width="650" style="background-color:transparent;width:650px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
                                <div class="col num12" style="min-width: 320px; max-width: 650px; display: table-cell; vertical-align: top; width: 650px;">
                                    <div style="width:100% !important;">
                                        <!--[if (!mso)&(!IE)]><!-->
                                        <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
                                            <!--<![endif]-->
                                            <table border="0" cellpadding="0" cellspacing="0" class="divider" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top" width="100%">
                                                <tbody>
                                                    <tr style="vertical-align: top;" valign="top">
                                                        <td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px;" valign="top">
                                                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" height="10" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 0px solid transparent; height: 10px; width: 100%;" valign="top" width="100%">
                                                                <tbody>
                                                                    <tr style="vertical-align: top;" valign="top">
                                                                        <td height="10" style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top"><span></span></td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                            <!--[if (!mso)&(!IE)]><!-->
                                        </div>
                                        <!--<![endif]-->
                                    </div>
                                </div>
                                <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                                <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
                            </div>
                        </div>
                    </div>
                    <div style="background-color:transparent;">
                        <div class="block-grid two-up no-stack" style="Margin: 0 auto; min-width: 320px; max-width: 650px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: #FFFFFF;">
                            <div style="border-collapse: collapse;display: table;width: 100%;background-color:#FFFFFF;">
                                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:650px"><tr class="layout-full-width" style="background-color:#FFFFFF"><![endif]-->
                                <!--[if (mso)|(IE)]><td align="center" width="325" style="background-color:#FFFFFF;width:325px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 25px; padding-top:25px; padding-bottom:25px;"><![endif]-->
                                <div class="col num6" style="min-width: 320px; max-width: 325px; display: table-cell; vertical-align: top; width: 325px;">
                                    <div style="width:100% !important;">
                                        <!--[if (!mso)&(!IE)]><!-->
                                        <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:25px; padding-bottom:25px; padding-right: 0px; padding-left: 25px;">
                                            <!--<![endif]-->
                                            <div align="left" class="img-container left fixedwidth" style="padding-right: 0px;padding-left: 0px;">
                                                <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr style="line-height:0px"><td style="padding-right: 0px;padding-left: 0px;" align="left"><![endif]--><img alt="Image" border="0" class="left fixedwidth" src="http://cdn.mcauto-images-production.sendgrid.net/92f4cab4130b7228/6ac70d4b-6462-4a67-ac30-faec499c6d4f/256x105.png" style="text-decoration: none; -ms-interpolation-mode: bicubic; border: 0; height: auto; width: 100%; max-width: 195px; display: block;" title="Image" width="195" />
                                                <!--[if mso]></td></tr></table><![endif]-->
                                            </div>
                                            <!--[if (!mso)&(!IE)]><!-->
                                        </div>
                                        <!--<![endif]-->
                                    </div>
                                </div>
                                <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                                <!--[if (mso)|(IE)]></td><td align="center" width="325" style="background-color:#FFFFFF;width:325px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 25px; padding-left: 0px; padding-top:25px; padding-bottom:25px;"><![endif]-->
                                <div class="col num6" style="min-width: 320px; max-width: 325px; display: table-cell; vertical-align: top; width: 325px;">
                                    <div style="width:100% !important;">
                                        <!--[if (!mso)&(!IE)]><!-->
                                        <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:25px; padding-bottom:25px; padding-right: 25px; padding-left: 0px;">
                                            <!--<![endif]-->
                                            <div align="right" class="button-container" style="padding-top:10px;padding-right:0px;padding-bottom:10px;padding-left:10px;">
                                                <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing: 0; border-collapse: collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;"><tr><td style="padding-top: 10px; padding-right: 0px; padding-bottom: 10px; padding-left: 10px" align="right"><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="#" style="height:31.5pt; width:115.5pt; v-text-anchor:middle;" arcsize="34%" stroke="false" fillcolor="#0088ff"><w:anchorlock/><v:textbox inset="0,0,0,0"><center style="color:#ffffff; font-family:Tahoma, Verdana, sans-serif; font-size:14px"><![endif]-->
                                               
                                                <!--[if mso]></center></v:textbox></v:roundrect></td></tr></table><![endif]-->
                                            </div>
                                            <!--[if (!mso)&(!IE)]><!-->
                                        </div>
                                        <!--<![endif]-->
                                    </div>
                                </div>
                                <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                                <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
                            </div>
                        </div>
                    </div>
                    <div style="background-color:transparent;">
                        <div class="block-grid" style="Margin: 0 auto; min-width: 320px; max-width: 650px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: #D6E7F0;">
                            <div style="border-collapse: collapse;display: table;width: 100%;background-color:#D6E7F0;">
                                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:650px"><tr class="layout-full-width" style="background-color:#D6E7F0"><![endif]-->
                                <!--[if (mso)|(IE)]><td align="center" width="650" style="background-color:#D6E7F0;width:650px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 25px; padding-left: 25px; padding-top:5px; padding-bottom:60px;"><![endif]-->
                                <div class="col num12" style="min-width: 320px; max-width: 650px; display: table-cell; vertical-align: top; width: 650px;">
                                    <div style="width:100% !important;">
                                        <!--[if (!mso)&(!IE)]><!-->
                                        <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:60px; padding-right: 25px; padding-left: 25px;">
                                            <!--<![endif]-->
                                            <div align="center" class="img-container center fixedwidth" style="padding-right: 0px;padding-left: 0px;">
                                                <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr style="line-height:0px"><td style="padding-right: 0px;padding-left: 0px;" align="center"><![endif]-->
                                                <div style="font-size:1px;line-height:45px"> </div><img align="center" alt="Image" border="0" class="center fixedwidth" src="http://cdn.mcauto-images-production.sendgrid.net/92f4cab4130b7228/48bc327b-a5f2-40e0-80d4-ff98d66ffec1/1129x619.png" style="text-decoration: none; -ms-interpolation-mode: bicubic; border: 0; height: auto; width: 100%; max-width: 540px; display: block;" title="Image" width="540" />
                                                <!--[if mso]></td></tr></table><![endif]-->
                                            </div>
                                            <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 15px; padding-top: 20px; padding-bottom: 0px; font-family: Tahoma, Verdana, sans-serif"><![endif]-->
                                            <div style="color:#052d3d;font-family:Lato, Tahoma, Verdana, Segoe, sans-serif;line-height:1.5;padding-top:20px;padding-right:10px;padding-bottom:0px;padding-left:15px;">
                                                <div style="font-size: 12px; line-height: 1.5; font-family: Lato, Tahoma, Verdana, Segoe, sans-serif; color: #052d3d; mso-line-height-alt: 18px;">
                                                    <p style="font-size: 50px; line-height: 1.5; text-align: center; font-family: inherit; word-break: break-word; mso-line-height-alt: 75px; margin: 0;"><span style="font-size: 50px;"><strong><span style="font-size: 50px;"><span style="font-size: 38px;">WELCOME</span></span>
                                                        </strong>
                                                        </span>
                                                    </p>
                                                    <p style="font-size: 34px; line-height: 1.5; text-align: center; font-family: inherit; word-break: break-word; mso-line-height-alt: 51px; margin: 0;"><span style="font-size: 34px;"><strong><span style="font-size: 34px;"><span style="color: #2190e3; font-size: 34px;">'''+str(i[2]).upper()+''' '''+str(i[3]).upper()+'''</span></span>
                                                        </strong>
                                                        </span>
                                                    </p>
                                                </div>
                                            </div>
                                            <!--[if mso]></td></tr></table><![endif]-->
                                            <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px; font-family: Tahoma, Verdana, sans-serif"><![endif]-->
                                            <div style="color:#555555;font-family:Lato, Tahoma, Verdana, Segoe, sans-serif;line-height:1.2;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
                                                <div style="font-size: 12px; line-height: 1.2; color: #555555; font-family: Lato, Tahoma, Verdana, Segoe, sans-serif; mso-line-height-alt: 14px;">
                                                    <p style="font-size: 18px; line-height: 1.2; text-align: center; word-break: break-word; mso-line-height-alt: 22px; margin: 0;"><span style="font-size: 18px; color: #000000;">You Are Invited To Join Alumni Association Of Goa From <b>'''+str(i[7])+'''</b>. Please Click On The "JOIN NOW" Button To Join.</span></p>
                                                </div>
                                            </div>
                                            <!--[if mso]></td></tr></table><![endif]-->
                                            <div align="center" class="button-container" style="padding-top:20px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
                                                <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing: 0; border-collapse: collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;"><tr><td style="padding-top: 20px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px" align="center"><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="#" style="height:39pt; width:220.5pt; v-text-anchor:middle;" arcsize="29%" stroke="false" fillcolor="#fc7318"><w:anchorlock/><v:textbox inset="0,0,0,0"><center style="color:#ffffff; font-family:Tahoma, Verdana, sans-serif; font-size:16px"><![endif]--><a href="'''+app_base_url+'''alumni/custom/invitation/'''+str(i[16])+'''" style="-webkit-text-size-adjust: none; text-decoration: none; display: inline-block; color: #ffffff; background-color: #fc7318; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; width: auto; width: auto; border-top: 1px solid #fc7318; border-right: 1px solid #fc7318; border-bottom: 1px solid #fc7318; border-left: 1px solid #fc7318; padding-top: 10px; padding-bottom: 10px; font-family: Lato, Tahoma, Verdana, Segoe, sans-serif; text-align: center; mso-border-alt: none; word-break: keep-all;" target="_blank"><span style="padding-left:40px;padding-right:40px;font-size:16px;display:inline-block;"><span style="font-size: 16px; line-height: 2; word-break: break-word; mso-line-height-alt: 32px;"><strong>JOIN NOW</strong></span></span></a>
                                                <!--[if mso]></center></v:textbox></v:roundrect></td></tr></table><![endif]-->
                                            </div>
                                            <!--[if (!mso)&(!IE)]><!-->
                                        </div>
                                        <!--<![endif]-->
                                    </div>
                                </div>
                                <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                                <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
                            </div>
                        </div>
                    </div>
                    <div style="background-color:transparent;">
                        <div class="block-grid" style="Margin: 0 auto; min-width: 320px; max-width: 650px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: transparent;">
                            <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">
                                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:650px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
                                <!--[if (mso)|(IE)]><td align="center" width="650" style="background-color:transparent;width:650px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:20px; padding-bottom:60px;"><![endif]-->
                                <div class="col num12" style="min-width: 320px; max-width: 650px; display: table-cell; vertical-align: top; width: 650px;">
                                    <div style="width:100% !important;">
                                        <!--[if (!mso)&(!IE)]><!-->
                                        <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:20px; padding-bottom:60px; padding-right: 0px; padding-left: 0px;">
                                            <!--<![endif]-->
                                            <table cellpadding="0" cellspacing="0" class="social_icons" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" valign="top" width="100%">
                                                <tbody>
                                                    <tr style="vertical-align: top;" valign="top">
                                                        <td style="word-break: break-word; vertical-align: top; padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px;" valign="top">
                                                            <table align="center" cellpadding="0" cellspacing="0" class="social_table" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-tspace: 0; mso-table-rspace: 0; mso-table-bspace: 0; mso-table-lspace: 0;" valign="top">
                                                                <tbody>
                                                                    <tr align="center" style="vertical-align: top; display: inline-block; text-align: center;" valign="top">
                                                                        <td style="word-break: break-word; vertical-align: top; padding-bottom: 5px; padding-right: 8px; padding-left: 8px;" valign="top">
                                                                            <a href="https://www.facebook.com/darshpatelofficial" target="_blank"><img alt="Facebook" height="32" src="http://cdn.mcauto-images-production.sendgrid.net/92f4cab4130b7228/93ef56de-a14b-43c0-8cda-7ba7f3b69b19/64x64.png" style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: none; display: block;" title="Facebook" width="32" /></a>
                                                                        </td>
                                                                        <td style="word-break: break-word; vertical-align: top; padding-bottom: 5px; padding-right: 8px; padding-left: 8px;" valign="top">
                                                                            <a href="https://twitter.com/pateldarsh10" target="_blank"><img alt="Twitter" height="32" src="http://cdn.mcauto-images-production.sendgrid.net/92f4cab4130b7228/81c04100-cf31-4016-8820-9bf9296d39a0/64x64.png" style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: none; display: block;" title="Twitter" width="32" /></a>
                                                                        </td>
                                                                        <td style="word-break: break-word; vertical-align: top; padding-bottom: 5px; padding-right: 8px; padding-left: 8px;" valign="top">
                                                                            <a href="https://instagram.com/pateldarsh_007" target="_blank"><img alt="Instagram" height="32" src="http://cdn.mcauto-images-production.sendgrid.net/92f4cab4130b7228/858aeae3-142f-4b84-8400-87cc7e0e92d8/64x64.png" style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: none; display: block;" title="Instagram" width="32" /></a>
                                                                        </td>
                                                                        <td style="word-break: break-word; vertical-align: top; padding-bottom: 5px; padding-right: 8px; padding-left: 8px;" valign="top">
                                                                            <a href="mailto:mailto:alumni.association.goa@gmail.com" target="_blank"><img alt="E-Mail" height="32" src="http://cdn.mcauto-images-production.sendgrid.net/92f4cab4130b7228/89016f33-3bcf-4dc9-b8ee-a4b5bc249ea4/64x64.png" style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: none; display: block;" title="E-Mail" width="32" /></a>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                            <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px; font-family: Tahoma, Verdana, sans-serif"><![endif]-->
                                            <div style="color:#555555;font-family:Lato, Tahoma, Verdana, Segoe, sans-serif;line-height:1.5;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
                                                <div style="font-size: 12px; line-height: 1.5; color: #555555; font-family: Lato, Tahoma, Verdana, Segoe, sans-serif; mso-line-height-alt: 18px;">
                                                    <p style="font-size: 14px; line-height: 1.5; text-align: center; word-break: break-word; mso-line-height-alt: 21px; margin: 0;">© 2020 - Alumni Association Of Goa - All Rights Reserved.</p>
                                                </div>
                                            </div>
                                            <!--[if mso]></td></tr></table><![endif]-->
                                            <!--[if (!mso)&(!IE)]><!-->
                                        </div>
                                        <!--<![endif]-->
                                    </div>
                                </div>
                                <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                                <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
                            </div>
                        </div>
                    </div>
                    <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                </td>
            </tr>
        </tbody>
    </table>
    <!--[if (IE)]></div><![endif]-->
</body>

</html>
                '''
        try :
            mail.send(msg)
            mail_sent = 1
        except :
            print("Error In Sending Mail.")
            
        if mail_sent == 1 : 
            print("Invitation Mail Sent To :",str(i[4]))
            try :
                sql2 = "UPDATE students_added_by_college SET isEmailSent='YES' WHERE id=%d AND verification_code='%s'" % (int(user_id),str(verification_code))
                con.execute(sql2)
                cnx.commit()
                print("Updated isEmailSent In students_added_by_college to YES")
            except : 
                print("Unable To Update isEmailSent In students_added_by_college")
            
        else :   
            print("Error In Sending Invitation Mail Sent To :",str(i[4]))
    con.close()




@app.route('/',methods=['GET','POST'])
def ind():
    schedule.every(50).seconds.do(association_cron_for_alumni_email)
    schedule.every(30).seconds.do(association_cron_for_alumni_sms)
    schedule.every(10).seconds.do(college_bulk_registration)
    while True :
        schedule.run_pending()
        time.sleep(1)
    

    
if __name__ == "__main__" :
    # association_cron_for_alumni_email()
    app.run(host="127.0.0.1",port=5001,debug=True)


#--------------------------------------------------------------------------------
#--------------------------URL SHORTNER-----------------------------------------#

# from __future__ import with_statement                                                            
  
# import contextlib 
  
# try: 
#     from urllib.parse import urlencode           
  
# except ImportError: 
#     from urllib import urlencode 
# try: 
#     from urllib.request import urlopen 
  
# except ImportError: 
#     from urllib import urlopen 
  
# import sys 
  
  
# def make_tiny(url): 
#     request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':url}))     
#     with contextlib.closing(urlopen(request_url)) as response:                       
#         return response.read().decode('utf-8 ')                                       
  
# def main():                                                                 
#     for tinyurl in map(make_tiny, sys.argv[1:]):                    
#         print(tinyurl) 
  
# if __name__ == '__main__': 
#     main() 