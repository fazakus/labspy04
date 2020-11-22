print("=======================================")
print("===\t Nama \t : Faza Ardan Kusuma \t===")
print("===\t NIM \t : 312010001 \t\t\t===")
print("===\t Kelas \t : T1.20.B1 \t\t\t===")
print("=======================================")
print()
print("==========\t | Latihan |\t ==========")
print()

list1 = [0,1,2,3,4]
print(list1[2])
print(list1[1:4])
print(list1[4])
print(list1[3])
print()

list1[3] = 5
print(list1[3])
print()

list1[3:5] = [6,7]
print(list1)
print()

list2 = list1[3:5]
print(list2)
print()

list2.append("angka")
print(list2)
print()

list2.append([10, 11, "puluhan"])
print(list2)
print()

list3 = list1 + list2
print(list3)