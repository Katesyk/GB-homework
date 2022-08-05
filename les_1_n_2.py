seconds = 22562
s = seconds % 60
m = s // 60
h = seconds // 3600
print(f"Time: {h:02}:{m:02}:{s:02}")
