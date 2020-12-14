
family, each = input().split()
family = int(family)
each = int(each)
results = []
for x in range(family):
    f = []
    for y in range(each):
        height, width = input().split()
        height = float(height) / 3.28084
        weight = int(width)
        bmi = weight / (height ** 2)
        f.append(bmi)
    results.append(f)
    print()

for x in range(family):
    for y in range(each):
        if results[x][y] < 18.5:
            print("Family",(x+1),"mamber",(y+1),"is Under Weight according to",results[x][y],"index")
        elif 18.5 < bmi <= 24.9:
            print("Family",(x+1),"mamber",(y+1),"is Normal Weight according to",results[x][y],"index")
        else:
            print("Family",(x+1),"mamber",(y+1),"is Over Weight according to",results[x][y],"index")

        