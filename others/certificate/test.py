from PIL import Image,ImageDraw,ImageFont
import xlrd
ans = "<table border='1'>"
file_loc = "D:/ALUMNI_TRACKING_SYSTEM/certificate/Apptitude Zone_EUREKA-MATHS.xlsx"
file = xlrd.open_workbook(file_loc)
sheet = file.sheet_by_index(0)

recipients = []

for i in range(sheet.nrows):
    ans += "<tr>"    
    temp = []    
    for j in range(1):
        if i == 0 :
            pass
            # ans += "<th style='padding:10px;'>"+str(sheet.cell_value(i,6))+"</th>"
        else :
            name = sheet.cell_value(i,1) + " " + sheet.cell_value(i,2)
            email = sheet.cell_value(i,5)
            temp.append(name)
            temp.append(email)
    if len(temp) != 0 :
        recipients.append(temp)
    
# print(recipients)


font_type = ImageFont.truetype('D:/ALUMNI_TRACKING_SYSTEM/certificate/Vera.ttf',30)



names = [recipients[i][0] for i in range(len(recipients))]
# print(names)
print('Total : ',len(names))
poss = [ str(i) for i in range(len(recipients))]
# events = ["POSTER PRESENTATION","PROJECT PRESENTATION","PAPER PRESENTATION","EUREKA-E-MATHS","TECH ROADIES","ANGULAR JS"]
events = [recipients[i][1] for i in range(len(recipients))]
for i in range(len(names)):
    img = Image.open('D:/ALUMNI_TRACKING_SYSTEM/certificate/AAG_Certificate.JPG')
    
    # name = names[i].center(105," ") # 60
    # pos = poss[i].center(20," ") # 10
    # event = events[i].center(137," ") # 78

    name = names[i].center(115," ")
    pos = "December , 2020.".center(20," ") # 10
    event = events[i].center(140," ")

    draw = ImageDraw.Draw(img)
    
    font_type = ImageFont.truetype('D:/ALUMNI_TRACKING_SYSTEM/certificate/Vera.ttf',30)
    draw.text(xy=(50,380),text=name,fill=(0,0,0),font=font_type)
    
    font_type = ImageFont.truetype('D:/ALUMNI_TRACKING_SYSTEM/certificate/Vera.ttf',26)
    draw.text(xy=(10,498),text=event,fill=(0,0,0),font=font_type)

    font_type = ImageFont.truetype('D:/ALUMNI_TRACKING_SYSTEM/certificate/Vera.ttf',22)
    draw.text(xy=(640,623),text=pos,fill=(0,0,0),font=font_type)

    img.save('D:/ALUMNI_TRACKING_SYSTEM/certificate/Demo_Certificate_'+str(i+1)+'.jpg')

# img.show()