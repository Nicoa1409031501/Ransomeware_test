from glob import iglob
import json
count=0
count1=0
for i in iglob("./Response_from_ChatGPT/1st/*"):
    #print(i)
    #print(type(i))
    #print(i.split("\\",)[1])
    
    jsonFile_i = open(i,"r",encoding="utf8")
    dic_=json.load(jsonFile_i)
    
    if "choices" in dic_.keys():
        count+=1
        #print(dic_["choices"][0]["message"]["content"].splitlines()[0])
        if dic_["choices"][0]["message"]["content"].splitlines()[0] =="[可實現]":
            print(dic_["choices"][0]["message"]["content"])
            count1+=1
        else:print(dic_["choices"][0]["message"]["content"].splitlines()[0])
        
        #print(moemory)
        #_moemory1=Post_Prompt_Memorry(Assessment_ToT_stage_2,moemory)
        #with open("./Response_from_ChatGPT/2nd/"+i.split("\\",)[1],"w+",encoding="utf8") as file_json:
        #    json.dump(_moemory1.json(),file_json,indent=2, separators=(',', ':'),ensure_ascii=False)
    else:continue
print(count)
print(count1)