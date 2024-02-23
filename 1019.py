segundos = int(input())

hr = segundos // 3600
segundos %= 3600

mnt = segundos // 60
segundos %= 60

print(f'{hr}:{mnt}:{segundos}')