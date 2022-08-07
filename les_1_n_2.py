seconds = int(input("Введите секунды: "))
h = seconds // 3600
m = seconds % 3600 // 60
s = seconds % 60

print(f"Time: {h:02}:{m:02}:{s:02}")
