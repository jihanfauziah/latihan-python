USERNAME = "zihanfaujiah1616@gmail.com"
PASSWORD = "12345678"

username = input("masukan username\t: ")
password = input("masukan password\t: ")

if username != USERNAME:
    print("username tidak tersedia")
elif username == USERNAME and password != PASSWORD:
    print("Password salah")
else :
    print("Selamat datang ",username)