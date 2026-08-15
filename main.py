
f = open("Template/demo.txt")
x = f.read()
lines = x.splitlines()

failed = x.count("Failed")
invalid = x.count("Invalid user")
accepted = x.count("Accepted")
total = failed + invalid + accepted
threshold = 4
ips = {}

for words in lines:
    y = words.split()
    if "Failed" in words:
        ip = y[10]
        types = y[5]
    elif "Invalid user" in words:
        ip = y[9]
        types = " ".join(y[5:7])
    else:
        continue

    if ip not in ips:
        ips[ip] = {
        "Failed": 0,
        "Invalid user": 0
    }

    if types == "Failed":
        ips[ip]["Failed"] = ips[ip]["Failed"] + 1
    elif types == "Invalid user":
        ips[ip]["Invalid user"] = ips[ip]["Invalid user"] + 1


##################################################

print("==========================================")
print("          SSH LOG ANALYZER                ")
print("==========================================")
print()

print("📊 STATISTIQUES")
print("------------------------------------------")
print("Failed", "          :", failed)
print("Accepted","        :", accepted)
print("Invalid user","    :", invalid)
print("Total","           :", total)
print()

print("==========================================")
print("          ANALYSE DES IP                  ")
print("==========================================")
print()

for ip in ips:
    result_echec = ips[ip]["Failed"] + ips[ip]["Invalid user"]
    failure_threshold = result_echec >= threshold
    if failure_threshold:
        print("IP :", ip)
        print("Failed :", ips[ip]["Failed"])
        print("Invalid user :", ips[ip]["Invalid user"])
        print("Total :", result_echec)
        print(" 🚨 SUSPECTE")
        print()
    else:
        print("IP :", ip)
        print("Failed :", ips[ip]["Failed"])
        print("Invalid user :", ips[ip]["Invalid user"])
        print("Total :", result_echec)
        print()
        