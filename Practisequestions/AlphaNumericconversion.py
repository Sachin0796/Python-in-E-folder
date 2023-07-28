# given one print 1
# given two print 2
# number can be between 0 to 9999

# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 30 40 50 60 70 80 90 100 1000

valueDict={'zero':0,'one':1,'two':2, 'three': 3, 'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,
'eleven':11,'twelve':12,'thirteen':13,'forteen':14,'fifteen':15,'sixteen':16,'seventeen':17, 'eighteen':18
,'nineteen':19, 'twenty':20, 'thirty':30,'fourty':40, 'fifty':50, 'sixty':60, 'seventy':70, 'eighty':80, 'ninty':90,'hundred':100, 'thousand':1000}
def convertAlpha(alphaString):
    list=alphaString.split()
    if len(list)==1:
        return (valueDict[alphaString])        
    ans=0
    i=0  
    print(list)  
    while i<len(list)-1:
        if valueDict[list[i]]<10 and (valueDict[list[i+1]] == 100 or valueDict[list[i+1]]==1000):
            ans=ans+(valueDict[list[i]]*valueDict[list[i+1]])            
        elif valueDict[list[i]]>19 and valueDict[list[i+1]]<10:
            ans=ans+valueDict[list[i]]+valueDict[list[i+1]]
        i+=2        
    if len(list)%2!=0:
        ans  = ans + valueDict[list[len(list)-1]]
    return ans
print(convertAlpha("one thousand nine hundred ninty six"))