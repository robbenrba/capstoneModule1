# Libraries
import time
from tabulate import tabulate
from colorama import init, Fore

# Inisialisasi colorama
init(autoreset=True)

# Collection Data Types
dataBuku = [
    {'ID': 'TGGFF031603191925001', 'judul': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925, 'stockTotal': 32, 'stockAvailable': 22, 'stockRented': 10, 'harga': 1600},
    {'ID': '111GO010402131949001', 'judul': '1984', 'author': 'George Orwell', 'year': 1949, 'stockTotal': 12, 'stockAvailable': 10, 'stockRented': 2, 'harga': 155600},
    {'ID': 'TIRJS052202131951001', 'judul': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'year': 1951, 'stockTotal': 30, 'stockAvailable': 22, 'stockRented': 8, 'harga': 6300},
    {'ID': 'HTSJR064002121997001', 'judul': "Harry Potter and the Philosopher's Stone", 'author': 'J.K. Rowling', 'year': 1997, 'stockTotal': 18, 'stockAvailable': 10, 'stockRented': 8, 'harga': 199600},
    {'ID': 'TORJT052102141954001', 'judul': 'The Lord of the Rings', 'author': 'J.R.R. Tolkien', 'year': 1954, 'stockTotal': 42, 'stockAvailable': 22, 'stockRented': 20, 'harga': 17200},
    {'ID': 'TTGDA063602131979001', 'judul': "The Hitchhiker's Guide to the Galaxy", 'author': 'Douglas Adams', 'year': 1979, 'stockTotal': 42, 'stockAvailable': 22, 'stockRented': 20, 'harga': 18800}
]

dictMenu = {
'menu':(
 'Membaca Data Buku',           # READ
 'Menambah Buku Baru',          # CREATE
 'Menghapus Data Buku',         # DELETE
 'Edit Data Buku',              # UPDATE
 'Pencarian, Sort, dan Filter Data Buku',   # Sort, Filter [READ and/or UPDATE]
 'Meminjam Buku',               # Domain feature 1
 'Mengembalikan Buku',          # Domain feature 2
 'Exit Program'                 # EXIT
 ),                # Indentasi hanya untuk readability, bukan nested dict.
    'menuRead': (  # Sub menu ditambahkan opsi kembali dalam fungsi print menu
    'Menampilkan Semua Daftar Buku',
    'Menampilkan Entri Buku ID Tertentu'
    ),
    'menuCreate' : (
    'Tambah 1 Entri Buku',
    'Tambah Banyak Entri Buku'
    ),
    'menuDelete' : (
    'Hapus 1 Entri Buku',
    'Hapus Seluruh Data Buku'
    ),
    'menuUpdate' : (
    'Edit Entri Buku'
    ),
    'menuSortFilter' : (
    'Pencarian Entri Buku',
    'Sort Entri Buku',
    'Filter Entri Buku'
    ),   
        'menuFilter' : (
        'Filter N Data Pertama / Limit',
        'Filter Berdasar ID',
        'Filter Berdasar Nama',
        'Filter Berdasar Author',
        'Filter Berdasar Tahun',
        'Filter Berdasar Stock Total',
        'Filter Berdasar Stock Available',
        'Filter Berdasar Stock Rented',
        'Filter Berdasar Harga'
        ),
        'menuSort' : (
        'Sort Berdasar ID',
        'Sort Berdasar Nama',
        'Sort Berdasar Author',
        'Sort Berdasar Tahun',
        'Sort Berdasar Stock Total',
        'Sort Berdasar Stock Available',
        'Sort Berdasar Stock Rented',
        'Sort Berdasar Harga'
        ),
 } 

 # Utility Functions
def paddedStr(text, textLen=50, padChar='='):
    padLen = max(0, textLen - len(text))
    padding = padChar * (padLen // 2)
    padded = f"{padding} {text} {padding}\n"
    if len(padded) < textLen:
        padded += padChar
    return padded 

def printMenu(key):
    if key == 'menu':
        text = dictMenu[key]
    elif key == 'menuUpdate':
        text = [dictMenu[key],'Kembali']
    else:
        text = list(dictMenu[key])
        text.append('Kembali')
    for i in range(len(text)):
        print(f'{i+1}. {text[i]}')
    print('\n')

def printDaftar(printData):
    readData = printData.copy()
    # Indexing hanya untuk print
    for iter, val in enumerate(readData):
        val['index'] = iter
    print(tabulate(readData, headers="keys", tablefmt="fancy_grid"))

# Feature 1 - Read : read data di list of dictionaries dataBuku
def featureRead():
    while(True):
        print(paddedStr('Record Data Buku'))
        printMenu('menuRead')
        inputOpt = input(f"Silahkan masukkan nomor menu [1-{len(dictMenu['menuRead'])+1}] : ")
        if inputOpt == '1':   # Tampilkan seluruh data
            if len(dataBuku) == 0:
                print(Fore.RED + paddedStr('Error : Tidak Ada Data Buku',padChar='+'))
                continue  # Skip iterasi saat error        
            else:
                printDaftar(dataBuku)
        elif inputOpt == '2': # Tampilkan data tertentu
            if len(dataBuku) == 0:
                print(Fore.RED + paddedStr('Error : Tidak Ada Data Buku',padChar='+'))
                continue
            else:
                inputID = input('Masukkan ID\n(contoh : TTGDA-0636-0213-1979-001 atau TTGDA063602131979001) : ').replace('-', '')
                flagEmpty = True
                for i in range(len(dataBuku)):
                    if dataBuku[i]['ID'] == inputID:
                        flagEmpty = False
                        printDaftar([dataBuku[i]]) # Print 1 row match
                        break
                if flagEmpty == True:
                    print(Fore.RED + paddedStr('Error : Tidak Ada Data Buku',padChar='+'))
                    continue
        elif inputOpt == '3': # Kembali
            break
     
# Feature 2 - Create : menambah entri di dataBuku
def functionInputCreate(ID,new=True):
    judul = input("Masukkan Judul : ")
    author = input("Masukkan Author : ")
    year = int(input("Masukkan Tahun : "))
    stockTotal = int(input("Masukkan Stock Total : "))
    if new:
        stockAvailable = stockTotal
        stockRented = 0
    else:
        stockAvailable = int(input("Masukkan Stock Available : "))
        stockRented = int(input("Masukkan Stock Rented (yang sedang dipinjam) : "))
    harga = int(input("Masukkan Harga : "))
    return ({
                'ID' : ID,
                'judul' : judul,
                'author' : author,
                'year' : year,
                'stockTotal' : stockTotal,
                'stockAvailable' : stockAvailable,
                'stockRented' : stockRented,
                'harga' : harga 
            })

def featureCreate():
    while(True):
        print(paddedStr('Menambah Buku Baru'))
        printMenu('menuCreate')
        inputOpt = input(f"Silahkan masukkan nomor menu [1-{len(dictMenu['menuCreate'])+1}] : ")
        if inputOpt == '1':   # Tambah 1 data
            inputID = input('Masukkan ID\n(contoh : TTGDA-0636-0213-1979-001 atau TTGDA063602131979001) : ').replace('-', '')
            # Cek duplicate data by ID
            flagDuplicate = False
            for i in range(len(dataBuku)):
                if dataBuku[i]['ID'] == inputID:
                    print(Fore.RED + paddedStr('Error : Data Buku Sudah Ada',padChar='+'))
                    flagDuplicate = True
                    break
            if flagDuplicate == True:
                continue
            # Proses Create     
            tempData = functionInputCreate(inputID)
            while(True):
                inputSave = input('Apakah anda ingin menyimpan Data ? (y/n) : ').lower()
                if inputSave == 'y':
                    dataBuku.append(tempData)
                    print(Fore.GREEN + paddedStr('Data Tersimpan',padChar='!'))
                    break
                elif inputSave == 'n':
                    print(Fore.RED + paddedStr('Data Tidak Tersimpan',padChar='!'))
                    break
        elif inputOpt == '2': # Tambah banyak data
            inputID = input('Masukkan ID(s) dengan Delimiter comma (,)\n(contoh : TTGDA-0636-0213-1979-001,WUBBM-0529-0216-2009-004 atau TTGDA063602131979001,WUBBM052902162009004) : ').replace('-', '').split(',')
            inputID = list(set(inputID))
            # Cek duplicate data by ID dan ignore duplicates
            inputDuplicate = []
            for item in inputID:
                for i in range(len(dataBuku)):
                    if dataBuku[i]['ID'] == item:         
                        inputDuplicate.append(item)
            inputDuplicate = list(set(inputDuplicate))
            for item in inputDuplicate:
                inputID.remove(item)
            if inputID == []:
                print(Fore.RED + paddedStr('Error : Semua ID Data Buku Sudah Ada',padChar='+'))
                continue
            # Proses Create
            tempData = []
            for item in inputID:    
                result = functionInputCreate(item)
                tempData.append(result)
            while(True):
                inputSave = input('Apakah anda ingin menyimpan Data ? (y/n) ').lower()
                if inputSave == 'y':
                    dataBuku.extend(tempData)
                    print(Fore.GREEN + paddedStr('Data Tersimpan',padChar='!'))
                    break
                elif inputSave == 'n':
                    print(Fore.YELLOW + paddedStr('Data Tidak Tersimpan',padChar='!'))
                    break
        elif inputOpt == '3': # Kembali
            break

# Feature 3 - Delete : menghapus entri di dataBuku
def featureDelete():
    while(True):
        print(paddedStr('Menghapus Data Buku'))
        printMenu('menuDelete')
        inputOpt = input(f"Silahkan masukkan nomor menu [1-{len(dictMenu['menuDelete'])+1}] : ")
        if inputOpt == '1':   # Delete 1 data
            inputID = input('Masukkan ID\n(contoh : TTGDA-0636-0213-1979-001 atau TTGDA063602131979001) : ').replace('-', '')
            # Cek data ada
            flagEmpty = True
            for i in range(len(dataBuku)):
                if dataBuku[i]['ID'] == inputID:
                    if flagEmpty == True: # Print header table saat match pertama dan flag masih empty
                        print('Deleting : \n')
                    flagEmpty = False
                    printDaftar([dataBuku[i]])
                    indexDel = i
                    break
            if flagEmpty == True:
                print(Fore.RED + paddedStr('Error : Tidak Ada Data Buku',padChar='+'))
                continue
            # Proses Delete     
            while(True):
                inputSave = input('Apakah anda ingin menghapus Data ? (y/n) ').lower()
                if inputSave == 'y':
                    dataBuku.pop(indexDel)
                    print(Fore.GREEN + paddedStr('Data Terhapus',padChar='!'))
                    break
                elif inputSave == 'n':
                    print(Fore.YELLOW + paddedStr('Data Tidak Terhapus',padChar='!'))
                    break
        elif inputOpt == '2': # Delete semua data
            # Proses Delete     
            while(True):
                inputSave = input('Apakah anda ingin menghapus Data ? (y/n) ').lower()
                if inputSave == 'y':
                    dataBuku.clear()
                    print(Fore.GREEN + paddedStr('Semua Data Terhapus',padChar='!'))
                    break
                elif inputSave == 'n':
                    print(Fore.YELLOW + paddedStr('Data Tidak Terhapus',padChar='!'))
                    break
        elif inputOpt == '3': # Kembali
            break

# Feature 4 - Update : edit data di dataBuku
def featureUpdate():
    while(True):
        print(paddedStr('Update Data Buku'))
        printMenu('menuUpdate')
        inputOpt = input(f"Silahkan masukkan nomor menu [1-{len(dictMenu['menuUpdate'])+1}] : ")
        if inputOpt == '1':   # Update 1 data
            inputID = input('Masukkan ID\n(contoh : TTGDA-0636-0213-1979-001 atau TTGDA063602131979001) : ').replace('-', '')
            # Cek data ada
            flagEmpty = True
            for i in range(len(dataBuku)):
                if dataBuku[i]['ID'] == inputID:
                    if flagEmpty == True: # Print header table saat match pertama dan flag masih empty
                        print('Updating : \n')
                    flagEmpty = False
                    printDaftar([dataBuku[i]])
                    indexUpdate = i
                    break
            if flagEmpty == True:
                print(Fore.RED + paddedStr('Error : Tidak Ada Data Buku',padChar='+'))
                continue
            # Proses Update     
            tempData = functionInputCreate(inputID,new=False)
            while(True):
                inputSave = input('Apakah anda ingin mengupdate Data ? (y/n) ').lower()
                if inputSave == 'y':
                    dataBuku[indexUpdate] = tempData
                    print(Fore.GREEN + paddedStr('Data diupdate',padChar='!'))
                    break
                elif inputSave == 'n':
                    print(Fore.YELLOW + paddedStr('Data Tidak diupdate',padChar='!'))
                    break
        elif inputOpt == '2': # Kembali
            break


# Feature 5 - Feature Pencarian, Sort, dan Filter
def functionFilter(key, keyword, search=False):
    if not search:
        filteredData = [buku for buku in dataBuku if keyword.lower() in str(buku[key]).lower()] # List comprehension untuk filter buku
    else:
        if len(dataBuku) !=0:
            filteredData = []
            for item in dataBuku[0].keys():
                filteredData = filteredData + [buku for buku in dataBuku if keyword.lower() in str(buku[item]).lower()]       
    return filteredData

def featurePencarian():
    print(paddedStr('Pencarian Data Buku'))
    keyword = input('Masukkan keyword : ')
    filteredData = functionFilter('',keyword,search=True)
    printDaftar(filteredData)

def featureFilter():
    readData = dataBuku.copy()
    while(True):
        print(paddedStr('Filter Data Buku'))
        printDaftar(readData)
        printMenu('menuFilter')

        inputOpt = input(f"Silahkan masukkan nomor menu [1-{len(dictMenu['menuFilter'])+1}] : ")
        if inputOpt == '1':
            keyword = int(input('Masukkan limit N baris: '))
            readData = readData[:keyword]
        elif inputOpt == '2':
            keyword = input('Masukkan ID : ')
            readData = functionFilter('ID',keyword)
        elif inputOpt == '3':
            keyword = input('Masukkan Judul : ')
            readData = functionFilter('judul',keyword)
        elif inputOpt == '4':
            keyword = input('Masukkan Author : ')
            readData = functionFilter('author',keyword)
        elif inputOpt == '5':
            keyword = input('Masukkan Tahun : ')
            readData = functionFilter('year',keyword)
        elif inputOpt == '6':
            keyword = input('Masukkan Stock Total : ')
            readData = functionFilter('stockTotal',keyword)
        elif inputOpt == '7':
            keyword = input('Masukkan Stock Available : ')
            readData = functionFilter('stockAvailable',keyword)
        elif inputOpt == '8':
            keyword = input('Masukkan Stock Rented : ')
            readData = functionFilter('stockRented',keyword)
        elif inputOpt == '9':
            keyword = input('Masukkan Harga : ')
            readData = functionFilter('harga',keyword)
        elif inputOpt == '10': # Kembali
            break

def featureSort():
    readData = dataBuku.copy()
    while(True):
        print(paddedStr('Sort Data Buku'))
        printDaftar(readData)
        printMenu('menuSort')

        inputOpt = input(f"Silahkan masukkan nomor menu [1-{len(dictMenu['menuSort'])+1}] : ")
        if inputOpt == '1':
            inputDesc = input(f"Apakah anda ingin sort Descending ? : (y/n) ")
            if inputDesc == 'y':
                readData.sort(key=lambda x: x['ID'], reverse=True)
            else:
                readData.sort(key=lambda x: x['ID'])
        elif inputOpt == '2':
            inputDesc = input(f"Apakah anda ingin sort Descending ? : (y/n) ")
            if inputDesc == 'y':
                readData.sort(key=lambda x: x['judul'], reverse=True)
            else:
                readData.sort(key=lambda x: x['judul'])
        elif inputOpt == '3':
            inputDesc = input(f"Apakah anda ingin sort Descending ? : (y/n) ")
            if inputDesc == 'y':
                readData.sort(key=lambda x: x['author'], reverse=True)
            else:
                readData.sort(key=lambda x: x['author'])
        elif inputOpt == '4':
            inputDesc = input(f"Apakah anda ingin sort Descending ? : (y/n) ")
            if inputDesc == 'y':
                readData.sort(key=lambda x: x['year'], reverse=True)
            else:
                readData.sort(key=lambda x: x['year'])
        elif inputOpt == '5':
            inputDesc = input(f"Apakah anda ingin sort Descending ? : (y/n) ")
            if inputDesc == 'y':
                readData.sort(key=lambda x: x['stockTotal'], reverse=True)
            else:
                readData.sort(key=lambda x: x['stockTotal'])
        elif inputOpt == '6':
            inputDesc = input(f"Apakah anda ingin sort Descending ? : (y/n) ")
            if inputDesc == 'y':
                readData.sort(key=lambda x: x['stockAvailable'], reverse=True)
            else:
                readData.sort(key=lambda x: x['stockAvailable'])
        elif inputOpt == '7':
            inputDesc = input(f"Apakah anda ingin sort Descending ? : (y/n) ")
            if inputDesc == 'y':
                readData.sort(key=lambda x: x['stockRented'], reverse=True)
            else:
                readData.sort(key=lambda x: x['stockRented'])
        elif inputOpt == '8':
            inputDesc = input(f"Apakah anda ingin sort Descending ? : (y/n) ")
            if inputDesc == 'y':
                readData.sort(key=lambda x: x['harga'], reverse=True)
            else:
                readData.sort(key=lambda x: x['harga'])
        elif inputOpt == '9': # Kembali
            break

def featureSortFilter(): # Sub menu Feature 5
    while(True):
        print(paddedStr('Pencarian, Sort, dan Filter Data Buku'))
        printMenu('menuSortFilter')
        inputOpt = input(f"Silahkan masukkan nomor menu [1-{len(dictMenu['menuSortFilter'])+1}] : ")
        if inputOpt == '1': # Pencarian (filter through all key)
            featurePencarian()
        elif inputOpt == '2': # Sort
            featureSort()
        elif inputOpt == '3': # Filter
            featureFilter()
        elif inputOpt == '4': # Kembali
            break

# Feature 6 - Feature Domain : melakukan proses peminjaman buku / rent
def featureRent(): 
    keranjang = []
    while(True): # Loop Pinjam lagi
        print(paddedStr('Peminjaman Buku'))
        printDaftar(dataBuku)
        inputID = input('Masukkan ID\n(contoh : TTGDA-0636-0213-1979-001 atau TTGDA063602131979001) : ').replace('-', '')
        # Cek data ada
        flagEmpty = True
        for i in range(len(dataBuku)):
            if dataBuku[i]['ID'] == inputID:
                flagEmpty = False
                indexRent = i
                break
        if flagEmpty == True:
            print(Fore.RED + paddedStr('Error : Tidak Ada Data Buku',padChar='+'))
            continue
        
        while True: # Loop peminjaman buku dan penyesuaian jumlah buku
            inputJmlRent = int(input(f"Silahkan masukkan jumlah buku ID {dataBuku[indexRent]['ID']} yang ingin dipinjam: "))
            if inputJmlRent <= dataBuku[indexRent]['stockAvailable']:
                dataBuku[indexRent]['stockAvailable'] = dataBuku[indexRent]['stockAvailable'] - inputJmlRent # kurangi stockAvailable
                dataBuku[indexRent]['stockRented'] = dataBuku[indexRent]['stockRented'] + inputJmlRent       # tambah stockRented
                break
            else:
                print('stock tidak memenuhi silahkan masukkan kembali jumlah bukunya')
        
        # Update Keranjang
        keranjang.append({
            'ID': dataBuku[indexRent]['ID'],
            'judul': dataBuku[indexRent]['judul'],
            'author': dataBuku[indexRent]['author'],
            'qty': inputJmlRent,
            'harga': dataBuku[indexRent]['harga']})
        printDaftar(keranjang)

        # Pinjam lagi continue / break condition
        inputRentLagi = str(input('Apakah Anda ingin pinjam buku yang lain ? (y/n) '))
        if inputRentLagi == 'y':
            continue
        else:
            # Hitung sum total
            totalHargaBayar = 0
            for item in keranjang:
                temp = item['qty']*item['harga']
                totalHargaBayar = totalHargaBayar + temp
                item['total'] = temp

            printDaftar(keranjang)
                
            print(f'\nTotal yang harus dibayar: Rp. {totalHargaBayar:,.2f}')
            # Loop pembayaran
            while True:
                inputUang = int(input('Masukkan jumlah uang: '))
                if inputUang > totalHargaBayar:
                    print(Fore.GREEN + f'Terima kasih !\n')
                    print(f'Uang kembalian anda sebesar : Rp. {inputUang - totalHargaBayar:,.2f}\n')
                    break
                elif inputUang == totalHargaBayar:
                    print(Fore.GREEN + f'Terima kasih !\n')
                    break
                else:
                    print(Fore.RED + f'Uang anda kurang sebesar : Rp. {totalHargaBayar - inputUang:,.2f}\n')
                    continue
            break 
    
    
# Feature 7 - Feature Domain : melakukan proses pengembalian buku / return
def featureReturn(): 
    bukuReturn = []
    printDaftar(dataBuku)
    while(True): # Loop Pengembalian lagi
        print(paddedStr('Pengembalian Buku'))
        inputID = input('Masukkan ID\n(contoh : TTGDA-0636-0213-1979-001 atau TTGDA063602131979001) : ').replace('-', '')
        # Cek data ada
        flagEmpty = True
        for i in range(len(dataBuku)):
            if dataBuku[i]['ID'] == inputID:
                flagEmpty = False
                indexRent = i
                break
        if flagEmpty == True:
            print(Fore.RED + paddedStr('Error : Tidak Ada Data Buku',padChar='+'))
            continue
        
        while True: # Loop pengembalian buku dan penyesuaian jumlah buku
            inputJmlRent = int(input(f"Silahkan masukkan jumlah buku ID {dataBuku[indexRent]['ID']} yang ingin dikembalikan: "))
            if inputJmlRent <= dataBuku[indexRent]['stockAvailable']:
                dataBuku[indexRent]['stockAvailable'] = dataBuku[indexRent]['stockAvailable'] + inputJmlRent # tambah stockAvailable
                dataBuku[indexRent]['stockRented'] = dataBuku[indexRent]['stockRented'] - inputJmlRent       # kurangi stockRented
                break
            else:
                print('stock tidak memenuhi silahkan masukkan kembali jumlah bukunya')
        
        # Update bukuReturn
        bukuReturn.append({
            'ID': dataBuku[indexRent]['ID'],
            'judul': dataBuku[indexRent]['judul'],
            'author': dataBuku[indexRent]['author'],
            'qty': inputJmlRent,
            'harga': dataBuku[indexRent]['harga']})
        printDaftar(bukuReturn)

        # Mengembalikan lagi continue / break condition
        inputRentLagi = str(input('Apakah Anda ingin mengembalikan buku yang lain ? (y/n) '))
        if inputRentLagi == 'y':
            continue
        else:
            print(Fore.GREEN + f'Terima kasih telah mengembalikan buku Anda !\n')
            break 


def mainMenu():
    while(True):
        print(paddedStr('Main Menu Aplikasi Perpustakaan'))
        print('Selamat Datang di Aplikasi Perpustakaan Robert !')
        print(Fore.YELLOW + 'Silahkan Maximize window cmd atau powershell untuk pengalaman optimal\n')
        printMenu('menu')
        inputOpt = input(f"Silahkan masukkan nomor menu [1-{len(dictMenu['menu'])}] : ")
        if inputOpt == '1':
            featureRead()
        elif inputOpt == '2':
            featureCreate()
        elif inputOpt == '3':
            featureDelete()
        elif inputOpt == '4':
            featureUpdate()
        elif inputOpt == '5':
            featureSortFilter()
        elif inputOpt == '6':
            featureRent()
        elif inputOpt == '7':
            featureReturn()  
        elif inputOpt == '8':
            print(Fore.GREEN + 'Terima kasih telah menggunakan aplikasi perpustakaan kami !')
            break
        else:
            print(Fore.YELLOW + 'Menu tidak tersedia, silahkan masukkan kembali', end=' ')
            time.sleep(1)
            print(Fore.RED + '.', end=' ')
            time.sleep(1)
            print(Fore.RED + '.', end=' ')
            time.sleep(1)
            print(Fore.RED + '.\n')
            continue

# Menjalankan aplikasi
mainMenu()
