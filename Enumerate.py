sabji=["Bhindi","Aloo","Chopstick","Manchurian"]
# sabji=["aloo"]
if len(sabji)==1:
    print(f"Jarvis, please buy {sabji[0]}")
elif len(sabji)==2:
    print(f"Jarvis, please buy {sabji[0]} and {sabji[1]}")
else:
    final="Jarvis, please buy "
    for item in sabji:
        if item==sabji[len(sabji)-1]:
            final=final[:len(final)-2:]+" & "+item
        else:
            final=final+item+", "
    print(final)


for index, item in enumerate(sabji):
    if index%2==0:
        print(item)