data_mahasiswa
    "Yusri Malagapi": "0735211021",
    "reza"  : "07352111036",
    "darwis"    : "07352211145",
    "muammar"   : "07352211180",
}
def login():
    username =input("masukan username:")
    password =input("masukan password:")
    if username in data_mahasiswa and data_mahasiswa [username].lower() == password.lower():
        print ("selamat datang, {}!".format(username))
    else:
        print("data yang anda masukan salah!")
        
while True:
    login()
    lanjut = input("coba lagi?) (y/t): ") 
    if lanjut.lower()== "t":
        break
print ("terima kasih!")