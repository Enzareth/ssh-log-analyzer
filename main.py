
f = open("Template/demo_v8_scenarios.txt")
x = f.read()
lines = x.splitlines()

failed = x.count("Failed")
invalid = x.count("Invalid user")
accepted = x.count("Accepted")
total = failed + invalid + accepted
ips = {}

for words in lines:
    y = words.split()
    if "Accepted" in words or "Failed" in words:
        ip = y[10]
        types = y[5]
    elif "Invalid user" in words:
        ip = y[9]
        types = " ".join(y[5:7])
    else:
        continue

    if ip not in ips:
        ips[ip] = {
        "Accepted": 0,    
        "Failed": 0,
        "Invalid user": 0
    }

    if types == "Failed":
        ips[ip]["Failed"] = ips[ip]["Failed"] + 1
    elif types == "Invalid user":
        ips[ip]["Invalid user"] = ips[ip]["Invalid user"] + 1
    elif types == "Accepted":
        ips[ip]["Accepted"] = ips[ip]["Accepted"] + 1

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
    result_types = ips[ip]["Failed"] + ips[ip]["Invalid user"] + ips[ip]["Accepted"]
    failure_rate = result_echec / result_types
    
    if failure_rate <= 1/3:
        print("IP :", ip)
        print("Failed :", ips[ip]["Failed"])
        print("Invalid user :", ips[ip]["Invalid user"])
        print("Accepted :", ips[ip]["Accepted"])
        print("Total :", result_types)
        print("🟢 Neutre")
        print()
    elif failure_rate > 1/3 and failure_rate <= 2/3:
        print("IP :", ip)
        print("Failed :", ips[ip]["Failed"])
        print("Invalid user :", ips[ip]["Invalid user"])
        print("Accepted :", ips[ip]["Accepted"])
        print("Total :", result_types)
        print("🟠 À surveiller")
        print()
    elif failure_rate > 2/3:
        print("🚨 IP :", ip)
        print("Failed :", ips[ip]["Failed"])
        print("Invalid user :", ips[ip]["Invalid user"])
        print("Accepted :", ips[ip]["Accepted"])
        print("Total :", result_types)
        print("🔴 Suspect")
        print()
