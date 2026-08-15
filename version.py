print("==========================================")
print("                V1                        ")
print("==========================================")
print("\n")

f = open("Template/demo.txt")
for ligne in f:
    print(ligne)
print("\n")

print("==========================================")
print("                V2                        ")
print("==========================================")
print("\n")

f = open("Template/demo.txt")
x = f.read()
a = x.count("Failed")
b = x.count("Invalid user")
c = x.count("Accepted")
e = a + b + c
print("Failed :", a)
print("Invalid user :", b)
print("Accepted :", c)
print("-------------------")
print("Total :", e)
print("\n")

print("==========================================")
print("                V3                        ")
print("==========================================")
print("\n")

f = open("Template/demo.txt")
x = f.read()
lines = x.splitlines()
for ligne in lines:
    c = ligne.split()
    if "Accepted" in ligne or "Failed" in ligne:
        print("Date :", c[0], c[1], c[2])
        print("Type :", c[5])
        print("Utilisateur :", c[8])
        print("IP :", c[10])
        print("Port :", c[12])
        print("\n")
    elif "Invalid user" in ligne:
        print("Date :", c[0], c[1], c[2])
        print("Type :", c[5], c[6])
        print("Utilisateur :", c[7])
        print("IP :", c[9])
        print("Port :", c[11])
        print("\n")

print("==========================================")
print("                V4                        ")
print("==========================================")
print("\n")

ips = {'19.1.1.1': 2, '19.1.1.2': 1}
x = ips.keys()
print("IP          Tentatives")
print("-----------------------")
for ip in x:
    print(ip, "  →", ips[ip])
print("\n")

f = open("Template/demo.txt")
x = f.read()
ips = {}
lines = x.splitlines()
for ligne in lines:
    c = ligne.split()
    if "Accepted" in ligne or "Failed" in ligne:
        ip = c[10]
    elif "Invalid user" in ligne:
        ip = c[9]
    if ip in ips:
            ips[ip] = ips[ip] + 1
    else:
        ips[ip] = 1

print("IP          Tentatives")
print("-----------------------")
x = ips.keys()
for ip in x:
    print(ip, "  →", ips[ip])

print("==========================================")
print("                V5                        ")
print("==========================================")
print("\n")

seuil = 4
f = open("Template/demo.txt")
x = f.read()
lines = x.splitlines()
ips = {}

for ligne in lines:
    c = ligne.split()
    if "Accepted" in ligne or "Failed" in ligne:
        ip = c[10]
    elif "Invalid user" in ligne:
        ip = c[9]
    if ip in ips:
            ips[ip] = ips[ip] + 1
    else:
        ips[ip] = 1

print("================================")       
print("         IP SUSPECTES")
print("================================")
x = ips.keys()
for ip in x:
    test = ips[ip] >= seuil
    if test: 
        print("🚨", ip, "→", ips[ip])

print("==========================================")
print("                V6                        ")
print("==========================================")
print("\n")


f = open("Template/demo.txt")
x = f.read()
lines = x.splitlines()
ips = {}

for lignes in lines:
    c = lignes.split()

    if "Failed" in lignes:
        ip = c[10]
        types = c[5]

    elif "Invalid user" in lignes:
        ip = c[9]
        types = " ".join(c[5:7])

    else:
        continue

    if ip not in ips:
        ips[ip] = {
        "Failed": 0,
        "Invalid user": 0
    }

    if ip not in ips:
        ips[ip] = {
            "Failed": 0,
            "Invalid user": 0
        }

    if types == "Failed":
        ips[ip]["Failed"] = ips[ip]["Failed"] + 1

    elif types == "Invalid user":
        ips[ip]["Invalid user"] = ips[ip]["Invalid user"] + 1


print("================================")
print("        ANALYSE DES ECHECS")
print("================================")

for ip in ips:
    print("IP :", ip)
    print("Failed :", ips[ip]["Failed"])
    print("Invalid user :", ips[ip]["Invalid user"])
    print()

print("==========================================")
print("                V7                        ")
print("==========================================")
print("\n")