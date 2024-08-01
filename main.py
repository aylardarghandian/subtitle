from googletrans import Translator
import os 

tr = Translator()
filepath="subtranslate"
filename1="subtitle.srt"
filename2="subtitle.txt"
nums=["1","2","3","4","5","6","7","8","9"]
with open(os.path.join(filepath,filename1)) as f:
    sub_line=f.readlines()
with open(os.path.join(filepath,filename2),'w', encoding="utf-8") as f:
    for line_en in sub_line:
        print(line_en)
        if line_en[0] in nums:
            f.write(line_en)
        elif line_en=="\n":
            f.write("\n")
        else:
            if line_en:
                 line_fa = tr.translate(line_en, src='en', dest='fa')
                 f.write(line_fa.text)
