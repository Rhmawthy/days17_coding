#pengenalan fungsi
#fungsi ini berfungsi membentu program menjadi program menjadi lebih ringkas

#fungsi dengan argument, fungsi ini dengan input

def pengenalan (materi):#fungsi pengenalan menerima argument/input dengan variabel materi


    print("selamat belajar pengenalan",materi) #kemudian argument akan hidup di badan fungsi

   
    
pengenalan("fungsi dengan argument") #saat kita panggil pengenalan string "fungsi dengan argument" stringnya akan masuk ke variabel materi/ke argument

#contoh kalkulator sederhana menggunakan argument
angka1 = int(input("enter the fists number:"))
operator = input( "+ , -, *, /" )
angka2 = int(input("enter the second number:"))
                   
def aritmatika (angka_1,angka_2):
    if operator == "+":
        print("hasil =", angka_1 + angka_2)
    elif operator == "-":
        print("hasil =", angka_1 - angka_2)
    
    elif operator == "*":
         print("hasil =", angka_1 * angka_2)
   
    elif operator == "/":
        print("hasil =", angka_1 / angka_2)
    
        

aritmatika (angka1,angka2)
    
