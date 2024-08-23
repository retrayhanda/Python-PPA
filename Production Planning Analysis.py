def cover():
    print(''' 
            ||=======================================================================================||
            ||                                                                                       ||
            ||                                                                                       ||
            ||                                                                                       ||
            ||                                                                                       ||
            ||              "ANALISIS PERENCANAAN PRODUKSI PADA PT. ARMSTRONG INDUSTRI               ||
            ||               INDONESIA DENGAN METODE FORECASTING DAN AGREGAT PLANNING"               ||  
            ||                                                                                       ||
            ||                                                                                       ||
            ||                                         OLEH:                                         ||
            ||                                                                                       ||   
            ||                                  RAHMAD HARET RAYHANDA                                ||
            ||                        PUTRI NURZAHIRA HAMIZAH Y.  (2310932028)                       ||
            ||                                                                                       ||                            
            ||                                                                                       || 
            ||                                                                                       ||
            ||=======================================================================================||
            
                                                                                                    ''')
cover()

from tabulate import tabulate

t  = ['Jan-','Feb-','Mar-','Apr-','May-','Jun-','Jul-','Aug-','Sep-','Oct-','Nov-','Des-']
ia = [537600,370800,508800,445200,471600,510000,600000,453600,439200,500400,499200,495600,505200,499200,398400,600000]
Fot = [618400,650000,232000,124400,214400,240000,300000,240000,200000,230000,320000,260000,500000,250000,80000,170000]
ssA = [103140,107520,70740,87260,94240,91760,94910,116385,60615,135000,138000,130420,145093,132007,71760,110900]
pekerja = 35
matcost = 630
gajiperog = 4160000
gajilem = 179740
pph = 6000
hkr = [20,21,22,23,20,23]
hkl = [8,8,9,9,13,8]
jmlprodlem = 1000
jpl = [17,9,13,10,18,9]

class Fungsi:
    def __init__(self,fu):
        self.fu = fu
    def agregat(self):
        self.fu = []
        for n in range(len(ia)):
            dA = ia[n]+Fot[n]+ssA[n]
            self.fu.append(dA)
    def sesft(self,a):
        self.fu = [(At.fu[0])]
        for n in range(len(ia)):
            dF = self.fu[n] + a*(At.fu[n] - self.fu[n])
            self.fu.append(dF)
    def ftlanjut(self):
        n = 0
        k = 2
        for n in range(n,6):
            dF = self.fu[-1]*k
            self.fu.append(dF)
            k = k + 1
    def et(self,D):
        self.fu = []
        for n in range(len(ia)):
            dE = (D.fu[n] - At.fu[n])**2
            self.fu.append(dE)
    def error(self,n,D):
        self.fu = []
        for n in range(n,len(ia)):
            dEr = abs(At.fu[n] - D.fu[n])
            self.fu.append(dEr)
    def pei(self,D):
        self.fu = []
        for n in range(len(ia)):
            dPEr = (D.fu[n]/At.fu[n])*100
            self.fu.append(dPEr)
    def smaft(self):
        self.fu = []
        n = 0
        while n < 3:
            self.fu.append(0)
            n = n + 1
        for n in range(n,len(ia)+1):
            dP3B = (At.fu[n-1]+At.fu[n-2]+At.fu[n-3])/3
            self.fu.append(dP3B)
    def biaskecil(self):
        sumperc = [((sum(D10.fu)/(len(D1.fu))), D1.fu, 'Single Exponential Smoothing dengan a = 0.1'), ((sum(D11.fu)/(len(D1.fu))), D2.fu, 'Single Exponential Smoothing dengan a = 0.2'),
                    ((sum(D12.fu)/(len(D1.fu))), D3.fu, 'Single Exponential Smoothing dengan a = 0.4'),((sum(D15.fu)/(len(D14.fu)-2)), D13.fu, 'Single Moving Average')]
        sumperc.sort()
        self.fu = sumperc[0][1]
    def lspp(self):
        self.fu = []
        for n in range(len(hkr)):
            dls = hkr[n]*pph
            self.fu.append(dls)
    def lsproduksi(self):
        self.fu = []
        for n in range(len(pp.fu)):
            dls = pekerja*pp.fu[n]
            self.fu.append(dls)
    def lsinventory(self,D):
        self.fu = []
        for n in range(len(pp.fu)):
            dls = abs(Dmin.fu[n+len(At.fu)]-D.fu[n])
            self.fu.append(dls)
    def lsbiayap(self,D):
        self.fu = []
        for n in range(len(pp.fu)):
            dls = matcost*D.fu[n]
            self.fu.append(dls)
    def lstotal(self,D):
        self.fu = []
        for n in range(len(pp.fu)):
            dls = D.fu[n]+(pekerja*gajiperog)
            self.fu.append(dls)
    def totlem(self):
        for n in range(len(jpl)):
            dms = jpl[n]*jmlprodlem
            self.fu.append(dms)
    def totsel(self,D,Dj):
        self.fu = []
        for n in range(len(jpl)):
            dms = D.fu[n]+Dj.fu[n]
            self.fu.append(dms)
    def biayalem(self):
        self.fu = []
        for n in range(len(jpl)):
            dms = jpl[n]*gajilem
            self.fu.append(dms)
    def totalms(self,D,Dj):
        self.fu = []
        for n in range(len(jpl)):
            dms = D.fu[n]+Dj.fu[n]+(pekerja*gajiperog)
            self.fu.append(dms)
    def hapus():
        while True:
            inpp = int(input('Berapa periode data baru yang akan diinputkan?(minimal 4) '))
            if inpp < 4:
                print('Minimal 4!')
            else:
                ia.clear()
                Fot.clear()
                ssA.clear()
                for i in range(inpp):
                    print('Data produk untuk periode',i+1,':')
                    dia = int(input('Insulation Sheet A: '))
                    dFot = int(input('Foot: '))
                    dssA = int(input('Stopper Support A: '))
                    ia.append(dia)
                    Fot.append(dFot)
                    ssA.append(dssA)
                    print()
                At.agregat()
                D1.sesft(0.1);D1.ftlanjut()
                D2.sesft(0.2);D2.ftlanjut()
                D3.sesft(0.4);D3.ftlanjut()
                D4.et(D1);D5.et(D2);D6.et(D3)
                D7.error(0,D1);D8.error(0,D2);D9.error(0,D3)
                D10.pei(D7);D11.pei(D8);D12.pei(D9)
                D13.smaft();D13.ftlanjut()
                D14.error(3,D13)
                D14.fu = [0]*3 + D14.fu
                D15.pei(D14)
                Dmin.biaskecil()
                pp.lspp()
                D16.lsproduksi()
                D17.lsinventory(D16)
                D18.lsbiayap(D16)
                D19.lstotal(D18)
                D21.totsel(D16,D20)
                D22.lsbiayap(D21)
                D23.biayalem()
                D24.totalms(D22,D23)
                print('Data sudah berhasil diubah!')
                break

    def hapus2():
        global gajiperog,matcost,gajilem,pph
        gajiperog = int(input('Gaji pekerja/ org: Rp '))
        matcost = int(input('Material cost/unit: Rp '))
        gajilem = int(input('Gaji lembur/ hari: Rp '))
        pph = int(input('Produk/pekerja/hari: '))
        pp.lspp()
        D16.lsproduksi()
        D17.lsinventory(D16)
        D18.lsbiayap(D16)
        D19.lstotal(D18)
        D21.totsel(D16,D20)
        D22.lsbiayap(D21)
        D23.biayalem()
        D24.totalms(D22,D23)
        print('Data sudah berhasil diubah!')

At = Fungsi([])
At.agregat()
D1 = Fungsi([]);D2 = Fungsi([]);D3 = Fungsi([])
D1.sesft(0.1);D1.ftlanjut()
D2.sesft(0.2);D2.ftlanjut()
D3.sesft(0.4);D3.ftlanjut()
D4 = Fungsi([]);D5 = Fungsi([]);D6 = Fungsi([])
D4.et(D1);D5.et(D2);D6.et(D3)
D7 = Fungsi([]);D8 = Fungsi([]);D9 = Fungsi([])
D7.error(0,D1);D8.error(0,D2);D9.error(0,D3)
D10 = Fungsi([]);D11 = Fungsi([]);D12 = Fungsi([])
D10.pei(D7);D11.pei(D8);D12.pei(D9)
D13 = Fungsi([]);D13.smaft();D13.ftlanjut()
D14 = Fungsi([])
D14.error(3,D13)
D14.fu = [0]*3 + D14.fu
D15 = Fungsi([])
D15.pei(D14)
Dmin = Fungsi([])
Dmin.biaskecil()
pp = Fungsi([])
pp.lspp()
D16 = Fungsi([])
D16.lsproduksi()
D17 = Fungsi([])
D17.lsinventory(D16)
D18 = Fungsi([])
D18.lsbiayap(D16)
D19 = Fungsi([])
D19.lstotal(D18)
D20 = Fungsi([])
D20.totlem()
D21 = Fungsi([])
D21.totsel(D16,D20)
D22 = Fungsi([])
D22.lsbiayap(D21)
D23 = Fungsi([])
D23.biayalem()
D24 = Fungsi([])
D24.totalms(D22,D23)

def main():
    while True:
        print('================================================================')
        print("|● PERENCANAAN PRODUKSI PADA PT. ARMSTRONG INDUSTRI INDONESIA ●|")
        print("|1. Data Penjualan Produk                                      |")
        print("|2. Perhitungan dengan Single Exponential Smoothing            |")
        print("|3. Peramalan dengan Single Moving Average                     |")
        print("|4. Rekapitulasi hasil peramalan                               |")
        print("|5. Stategi perencanaan Agregat                                |")
        print("|6. Ubah pendataan                                             |")
        print("|7. Akhiri Program                                             |")    
        print('================================================================')
        pilihan = int(input("Masukkan pilihan: "))
        if pilihan==1:
            no = [i+5 for i in range(len(ia))]
            periode = [t[(n+9)%len(t)]+str(17+((n+9)//12)) for n in range(len(ia))]

            data = zip(no, periode, ia, Fot, ssA, At.fu)
            headers = ["Nomor", "Periode", "Insulation Sheet","Foot","Stopper Support","Agregat"]
            tabel = tabulate(data, headers=headers, tablefmt="grid")
            print(tabel)
        elif pilihan==2:
            no = [i+1 for i in range(len(D1.fu))]
            periode = [t[(n+9)%len(t)]+str(17+((n+9)//12)) for n in range(len(D1.fu))]

            data = zip(no, periode, At.fu+[0,0,0,0,0,0],D1.fu,D2.fu,D3.fu,D4.fu+[0,0,0,0,0,0],D5.fu+[0,0,0,0,0,0],D6.fu+[0,0,0,0,0,0])
            headers = ["Nomor", "Periode", '''Data\nPermintaan''',"Ft,a=0,1","Ft,a=0,2","Ft,a=0,4","Et,a=0,1","Et,a=0,2","Et,a=0,4"]
            tabel = tabulate(data, headers=headers,tablefmt="grid",floatfmt=".2f")
            print(tabel)
            print('| Total Et |','Et(a=0.1): ''%.2f'%sum(D4.fu)+',','Et(a=0.2): ''%.2f'%sum(D5.fu)+',','Et(a=0.4): ''%.2f'%sum(D6.fu))
            print()
            D7.fu = D7.fu+[0,0,0,0,0,0]
            D8.fu = D8.fu+[0,0,0,0,0,0]
            D9.fu = D9.fu+[0,0,0,0,0,0]
            D10.fu = D10.fu+[0,0,0,0,0,0]
            D11.fu = D11.fu+[0,0,0,0,0,0]
            D12.fu = D12.fu+[0,0,0,0,0,0]
            data = zip(D7.fu,D8.fu,D9.fu,D10.fu,D11.fu,D12.fu)
            headers = ["error,a=0,1","error,a=0,2","error,a=0,4","PEI(%),a=0,1","PEI(%),a=0,2","PEI(%),a=0,4"]
            tabel = tabulate(data, headers=headers,tablefmt="grid",floatfmt=(".2f",".2f",".2f",".0f",".0f",".0f"))
            print(tabel)
            print('| Total error |','ei(a=0.1): ''%.2f'%sum(D7.fu)+',','ei(a=0.2): ''%.2f'%sum(D8.fu)+',','ei(a=0.4): ''%.2f'%sum(D9.fu))
            print('| MAE         |','ei(a=0.1): ''%.2f'%(sum(D7.fu)/(len(D1.fu)))+',','ei(a=0.2): ''%.2f'%(sum(D8.fu)/(len(D1.fu)))+',','ei(a=0.4): ''%.2f'%(sum(D9.fu)/(len(D1.fu))))
            print()
            print('| Total PEI   |','pei(a=0.1): ''%.0f'%sum(D10.fu)+'%,','pei(a=0.2): ''%.0f'%sum(D11.fu)+'%,','pei(a=0.4): ''%.0f'%sum(D12.fu)+'%,')
            print('| MAPE        |','pei(a=0.1): ''%.0f'%(sum(D10.fu)/(len(D1.fu)))+'%,','pei(a=0.2): ''%.0f'%(sum(D11.fu)/(len(D1.fu)))+'%,','pei(a=0.4): ''%.0f'%(sum(D12.fu)/(len(D1.fu)))+'%,')
        elif pilihan==3:
            no = [i+1 for i in range(len(D1.fu))]
            periode = [t[(n+9)%len(t)]+str(17+((n+9)//12)) for n in range(len(D1.fu))]
            data = zip(no, periode, At.fu,D13.fu+[0,0,0,0,0,0],D14.fu+[0,0,0,0,0,0],D15.fu+[0,0,0,0,0,0])
            headers = ["Nomor", "Periode", '''Data\nPermintaan''',"Ft","error","PEI(%)"]
            tabel = tabulate(data, headers=headers,tablefmt="grid",floatfmt=".2f")
            print(tabel)
            print('| Total error |','%.2f'%sum(D14.fu))
            print('| MAE         |','%.2f'%(sum(D14.fu)/(len(D14.fu)-2)))
            print('| Total PEI   |','%.2f'%sum(D15.fu)+'%')
            print('| MAPE        |','%.2f'%(sum(D15.fu)/(len(D15.fu)-2))+'%')
            
        elif pilihan==4:
            print()
            data = [["Single Exponential Smoothing (a = 0.1)",sum(D7.fu)/(len(D1.fu)),(sum(D10.fu)/(len(D1.fu)))],["Single Exponential Smoothing (a = 0.2)",sum(D8.fu)/(len(D1.fu)),(sum(D11.fu)/(len(D1.fu)))],
                    ["Single Exponential Smoothing (a = 0.4)",sum(D9.fu)/(len(D1.fu)),(sum(D12.fu)/(len(D1.fu)))],
                    ["Single Moving Average",(sum(D14.fu)/(len(D14.fu)-2)),(sum(D15.fu)/(len(D14.fu)-2))]]
            headers = ["","MAE","MAPE"]
            datarp = [[apa,f"{nilai1:.2f}",f"{nilai2:.2f}%"]for apa,nilai1,nilai2 in data]
            tabel = tabulate(datarp, headers=headers,tablefmt="grid")
            print(tabel)
            print()
            sumperc = [((sum(D10.fu)/(len(D1.fu))), D1.fu, 'Single Exponential Smoothing dengan a = 0.1'), ((sum(D11.fu)/(len(D1.fu))), D2.fu, 'Single Exponential Smoothing dengan a = 0.2'),
                    ((sum(D12.fu)/(len(D1.fu))), D3.fu, 'Single Exponential Smoothing dengan a = 0.4'),((sum(D15.fu)/(len(D14.fu)-2)), D13.fu, 'Single Moving Average')]
            sumperc.sort()
            print(f'Dapat terlihat bahwa metode {sumperc[0][2]} memiliki nilai bias yang paling kecil.')
            print()

        elif pilihan==5:
            while True:
                print("● STRATEGI PERENCANAAN AGREGAT PADA PRODUKSI PADA PT. ARMSTRONG INDUSTRI INDONESIA ●\n1. Data Penunjang Perencanaan Agregat\n2. Level Strategy\n3. Chase Strategy\n4. Mixed Strategy\n5. Kembali")
                pilihan2=int(input('Masukkan Pilihan : '))
                if pilihan2==1:
                    print('> Data Awal')
                    data = [["Pekerja Saat ini",pekerja],["Hiring Cost(Rp)",0],["Firing Cost(Rp)",0],["Inventory Cost(Rp)",0],["Gaji pekerja/orang(Rp)",gajiperog],
                            ["Material cost/unit(Rp)",matcost],["Stockout cost",0],["Gaji lembur/hari(Rp)",gajilem],["Produk/pekerja/hari(Rp)",pph]]
                    tabel = tabulate(data, tablefmt="grid")
                    print(tabel)
        
                elif pilihan2==2:
                    periode = [t[(n+1)%len(t)]+'19' for n in range(len(pp.fu))]
                    v = pekerja*gajiperog
                    Dm = [Dmin.fu[n+len(At.fu)]for n in range(len(pp.fu))]
                    data = list(zip(periode, pp.fu,D16.fu,Dm,D17.fu,D18.fu,[0,0,0,0,0,0],[v,v,v,v,v,v],D19.fu))
                    headers = ["Periode", "Produk/\npekerja","produksi\n(unit)","demand\n(unit)","inventory\n(unit)","Biaya\nproduksi","Biaya\ninventory","Biaya gaji","Total Cost"]
                    datarp = [[kolom[0],kolom[1],kolom[2],kolom[3],kolom[4],f'Rp {kolom[5]}',f'Rp {kolom[6]}',f'Rp {kolom[7]}',f'Rp {kolom[8]}']for kolom in data]
                    tabel = tabulate(datarp, headers=headers,tablefmt="grid",floatfmt=(".0f",".0f",".0f",".0f",".2f",))
                    print(tabel)
                    print('| Total seluruh cost |','Rp',sum(D19.fu))
                    
                elif pilihan2==3:
                    periode = [t[(n+1)%len(t)]+'19' for n in range(len(pp.fu))]
                    v = pekerja*gajiperog
                    p = pekerja
                    Dm = [Dmin.fu[n+len(At.fu)]for n in range(len(pp.fu))]
                    data = list(zip(periode, [p,p,p,p,p,p],[0,0,0,0,0,0],[0,0,0,0,0,0],pp.fu,D16.fu,Dm,D17.fu,D18.fu,[0,0,0,0,0,0],[v,v,v,v,v,v],D19.fu))
                    headers = ["Periode","Jumlah\npekerja","Hiring","Firing" ,"Produk/\npekerja","produksi\n(unit)","demand\n(unit)","inventory\n(unit)","Biaya\nproduksi","Biaya\ninventory","Biaya gaji","Total Cost"]
                    datarp = [[kolom[0],kolom[1],kolom[2],kolom[3],kolom[4],kolom[5],kolom[6],kolom[7],f'Rp {kolom[8]}',f'Rp {kolom[9]}',f'Rp {kolom[10]}',f'Rp {kolom[11]}']for kolom in data]
                    tabel = tabulate(datarp, headers=headers,tablefmt="grid",floatfmt=".0f")
                    print(tabel)
                    print('| Total seluruh cost |','Rp',sum(D19.fu))
                    
                elif pilihan2==4:
                    periode = [t[(n+1)%len(t)]+'19' for n in range(len(pp.fu))]
                    v = pekerja
                    l = jmlprodlem
                    data = list(zip(periode, hkr,hkl,pp.fu,[l,l,l,l,l,l],[v,v,v,v,v,v],jpl,D16.fu,D20.fu))
                    headers = ["Periode","Hari\nKerja\nregular","Hari\nKerja\nlembur","Produk/\npekerja","Produksi\nlembur/\npekerja","jumlah\npekerja","jumlah\npekerja\nlembur","produksi\nreguler","produksi\nlembur"]
                    tabel = tabulate(data, headers=headers,tablefmt="grid")
                    print(tabel)
                    Dm = [Dmin.fu[n+len(At.fu)]for n in range(len(pp.fu))]
                    v = pekerja*gajiperog
                    data = list(zip(D21.fu,Dm,[0,0,0,0,0,0],D22.fu,[0,0,0,0,0,0],D23.fu,[v,v,v,v,v,v],D24.fu))
                    headers = ["Total\nkeseluruhan\nproduksi","demand","inventory","biaya produksi","biaya\ninventory","biaya\nlembur","gaji pekerja","Total biaya"]
                    datarp = [[kolom[0],kolom[1],kolom[2],f'Rp {kolom[3]}',f'Rp {kolom[4]}',f'Rp {kolom[5]}',f'Rp {kolom[6]}',f'Rp {kolom[7]}']for kolom in data]
                    tabel = tabulate(datarp, headers=headers,tablefmt="grid",floatfmt=".0f")
                    print(tabel)
                    print('| Total biaya produksi    | Rp',sum(D22.fu))
                    print('| Total biaya lembur      | Rp',sum(D23.fu))
                    print('| Total gaji pekerja      | Rp',pekerja*gajiperog*(len(pp.fu)))
                    print('| Total biaya keseluruhan | RP',sum(D24.fu))
                elif pilihan2==5:
                    break
                else:
                    print('Pilihan tidak valid. silahkan pilih antara angka 1 sampai 5!')
                    
        elif pilihan==6:
            while True:
                print('''
● Ubah Pendataan ●
1. Data Penjualan
2. Data Penunjang Perencanaan Agregat
3. Kembali''')
                pilihan = int(input('Pilihan: '))
                if pilihan == 1:
                    Fungsi.hapus()
                elif pilihan==2:
                    Fungsi.hapus2()
                elif pilihan==3:
                    break
                else:
                    print('Pilihan tidak valid. silahkan pilih antara angka 1 sampai 3!')
        elif pilihan==7:
            print ('mantap')
            break
        else:
            print('Pilihan tidak valid. silahkan pilih antara angka 1 sampai 7!')

def login():
    users = {}
    while True:
        print('==================')
        print('1. Registrasi Akun\n2. Login\n3. keluar')
        print('==================')
        pil = int(input('Masukkan pilihan: '))
        if pil == 1:
            print(20*"=","\n● Registrasi Akun ●")
            username = str(input("Username: "))
            if username in users:
                print("Username sudah ada. Coba username lain.")
                return
            password = str(input("Password: "))
            users[username] = password
            print ("Registrasi Berhasil!")
            print(20*"=")
        elif pil == 2:
            total_percobaan = 3
            if not users:
                print('Belum ada akun yang terdatar. Silahkan registrasi.')
                continue
            for percobaan in range(total_percobaan):
                print("● Login Akun ●")
                username_login = str(input("Masukkan username: "))
                password_login = input("Masukkan password: ")
                if username_login in users and users[username] == password_login:
                    print("Login berhasil!")
                    main()
                    return True
                else:
                    print(f"Kata sandi salah. Sisa percobaan: {total_percobaan - percobaan - 1}")
            print("Anda telah melebihi batas percobaan. Program berhenti.")
            return False
        elif pil == 3:
            print('baiklah')
            break
        else:
            print('pilihan dari 1 sampai 3!')
login()
