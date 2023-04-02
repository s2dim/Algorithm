n = 20

idx = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5,
       "C0":2.0, "D+":1.5, "D0":1.0, "F":0} 

total = []
scr_total = []

for i in range(n):
    lst = input()
    scr = lst[-6:-2].strip()
    scr = float(scr)
    grd = lst[-2:].strip()

    if grd == "P":
        pass
    else:
        grd = idx[grd]
        total.append(scr * grd)
        scr_total.append(scr)

print(sum(total) / sum(scr_total))