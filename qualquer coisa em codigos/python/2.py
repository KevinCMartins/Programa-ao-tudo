from time import sleep

c = 0
a = 0

print('Cortando cabos de uma bomba')

for c in range(10, 5, -1):
    print(c)
    sleep(1)
print('*cortou o cabo errado*')
sleep(2)

for a in range(5, 0, -1):
    print(a)
    sleep(0.1)
print('BOOM')