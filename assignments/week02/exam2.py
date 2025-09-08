prices = [25,15,32,8,45,13,67,23]

print("แพงสุด",max(prices))
print("ถูกที่สุด",min(prices))
print("result",sum(prices))
count = sum (1 for p in prices if p > 20)
print("จำนวนที่มากกว่า 20:", count)