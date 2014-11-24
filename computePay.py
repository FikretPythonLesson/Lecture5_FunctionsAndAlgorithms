try:
    inp = raw_input("Çalışma saatini girin: ")
    hours = float(inp)
    inp = raw_input("Saat ücretini girin: ")
    rate = float(inp)
except:
    print "Lütfen bir rakam girin"
    quit()

if hours <= 40:
    pay = rate * hours
else:
    pay = rate * 40 + ( rate * 1.5 * (hours - 40))

print pay
