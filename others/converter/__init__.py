import convertapi

PATH = ['RESUME_SAMPLES/RESUME_1.pdf','RESUME_SAMPLES/RESUME_2.pdf']

for i in range(len(PATH)) :
    convertapi.api_secret = 'jOQbkzhJV2zFsPq2'
    convertapi.convert('txt', {
        'File': PATH[i]
    }, from_format = 'pdf').save_files('CONVERTED/'+str(i+1)+'_extracted.txt')
    
    
CONVERTED_PATH = ['CONVERTED/1_extracted.txt','CONVERTED/2_extracted.txt']

KEYWORDS = ['python','programming','google']

for i in range(len(CONVERTED_PATH)) :
    FOUND_KEYWORDS = []
    print("="*50)
    print("File : ",CONVERTED_PATH[i])
        
    for j in range(len(KEYWORDS)) :
        f = open(CONVERTED_PATH[i],'r',encoding='utf-8').read().find(KEYWORDS[j])
        
        if f != -1 and KEYWORDS[j] not in FOUND_KEYWORDS:
            print("Keyword : ",KEYWORDS[j])
            FOUND_KEYWORDS.append(KEYWORDS[j])
    
    if len(FOUND_KEYWORDS) == 0 :
        print("Match : "+"0%")
    else :
        x = len(KEYWORDS)
        y = len(FOUND_KEYWORDS)
        
        percent = (100*y) / x
        
        print("Match : "+str(float(percent)))
        
            
        
        
    
    
  