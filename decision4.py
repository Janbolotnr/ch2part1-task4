chas, minuta, secunda = int(input("Enter chas 1: ")),int(input("Enter minuta 1: ")),int(input("Enter secunda 1: "))
chas2, minuta2, secunda2 = int(input("Enter chas 2: ")),int(input("Enter minuta 2: ")),int(input("Enter secunda 2: "))

time1 = chas * 3600 + minuta*60 + secunda
time2 = chas2 * 3600 + minuta2*60 + secunda2
result = (time1 - time2)
print(abs(result),"secunda")


#s1_sec = int(s1_sec[0])*3600+int(s1_sec[1])*60+int(s1_sec[2])
#s2_sec = int(s2_sec[0])*3600+int(s2_sec[1])*60+int(s2_sec[2])

#print(hour, minu, sec, "secund")

#h_sec1 = 11 * 3600
#h_sec2 = 22 * 3600
#ob_1 = 23 * 3600
#summa1 = h_sec1 + h_sec2
#hour = (ob_1 - summa1) // 3600
 
#print(h_sec1, h_sec2, summa1, ob_1)
#print(hour)


