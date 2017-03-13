mylist = ["uno", "dos", "tres", "cuatro"]
for i, item in enumerate(mylist, 1):
    print " id_%d : %s" % (i, item)

styles = []
calques = []
for i in calques:
    if i == 1:
        styles.append("0.13mm")
    elif i == 2:
        styles.append("0.25mm")
    elif i == 4:
        styles.append("0.35mm")
    else:
        styles.append("0")


styles.extend(["0.13mm", "0.25mm", "0.35mm"])
print styles
