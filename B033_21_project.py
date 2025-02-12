import matplotlib.pyplot as plt
import numpy as np

Literacy_rate=[]
fpr=open("Report_of_different_age.csv","r")
head=fpr.readline()
line=fpr.readline()
while (len(line)>0):
        arr=line.strip().split(',')
        Literacy_rate.append(float(arr[10]))
        line=fpr.readline()
fpr.close()
Literacy_rate_np=np.array(Literacy_rate)
mean_Literacy_rate=np.mean(Literacy_rate)
max_Literacy_rate=np.max(Literacy_rate)
min_Literacy_rate=np.min(Literacy_rate)

print(f"Mean Literacy rate of different age: {mean_Literacy_rate}")
print(f"Max Literacy rate of different age: {max_Literacy_rate}")
print(f"Min Literacy rate of different age: {min_Literacy_rate}")

plt.figure(figsize=(10,6))
plt.plot(Literacy_rate_np,label='Literacy_rate',color='blue',marker='o')
plt.title('Report of different age')
plt.xlabel('Index')
plt.ylabel('Literacy_rate')
plt.grid(True)
plt.legend()
plt.show()