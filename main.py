'''Module'''

import mysql.connector

'''DB Verbindung'''

verbindung = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="fuhrpark"
)

srccursor = verbindung.cursor()


'''Globale Variablen'''

usermessage = "\n\n##################################\n| >>> Bitte wählen Sie ein Menü:\n##################################\n\n 1 - Fahrer anzeigen\n 2 - Fahrer anlegen\n 3 - Fahrzeuge anzeigen\n 4 - Fahrzeug anlegen\n 5 - Fahrer löschen\n 6 - Fahrzeug löschen\n 7 - Programm beenden"
uservalue = 0
allowedFeatures = [1,2,3,4,5,6,7]
state = 1


'''Funktionen'''

def getFahrer():
    lfdid = 1
    print('\n>>> Vorhandene Fahrer:')
    srccursor.execute("SELECT * FROM fahrer")
    request = srccursor.fetchall()
    for row in request:
        print("\n>> Fahrer Nr: ", lfdid)
        print("ID: ", row[0])
        print("Name: ", row[1])
        print("Führerschein Nummer: ", row[2])
        print("Adresse: ", row[3])
        lfdid += 1

def getName():
    print("\n")
    id_name = input("Bitte geben Sie den Namen an: ")
    return id_name

def getFSNR():
    print("\n")
    fsnr = input("Bitte geben Sie die Führerscheinnr an: ")
    return fsnr

def getAdresse():
    print("\n")
    addr = input("Bitte geben Sie die Adresse an: ")
    return addr

def createFahrer():
    print("\n")
    print('### Fahrer wird angelegt ###')
    sql = "INSERT INTO fahrer (Name, Fuehrerscheinnr, Adresse) VALUES (%s, %s, %s)"
    val = (getName(), getFSNR(), getAdresse())
    srccursor.execute(sql, val)
    verbindung.commit()

def getVehicles():
    lfdid = 1
    print("\n")
    print('>>> Fahrzeuge werden angezeigt: ')
    srccursor.execute("SELECT * FROM fahrzeug")
    request = srccursor.fetchall()
    for row in request:
        print("\n")
        print(">> Fahrzeug Nr: ", lfdid)
        print("Kennzeichen: ", row[0])
        print("Makre: ", row[1])
        print("Modell: ", row[2])
        print("Baujahr: ", row[3])
        lfdid += 1

def getKennzeichen():
    print("\n")
    plate = input("Bitte geben Sie das Kennzeichen an: ")
    return plate

def getMarke():
    print("\n")
    manuf = input("Bitte geben Sie die Marke an: ")
    return manuf

def getModell():
    print("\n")
    model = input("Bitte geben Sie das Modell an: ")
    return model

def getBaujahr():
    print("\n")
    year = input("Bitte geben Sie das Baujahr an: ")
    return year

def createFahrzeug():
    print("\n")
    print('### Fahrzeug wird angelegt ### \n')
    sql = "INSERT INTO fahrzeug (ID_Kennzeichen, Marke, Modell, Baujahr) VALUES (%s, %s, %s, %s)"
    val = (getKennzeichen(), getMarke(), getModell(), getBaujahr())
    srccursor.execute(sql, val)
    verbindung.commit()

def deleteFahrer():

    print("\n### Fahrer löschen ###")

    getFahrer()

    while True:
        try:
            FHR_UserChoice = int(input("\n>>> Geben Sie die ID des zu löschenden Fahrers an: "))
            break
        except:
            print('\n Die Eingabe sollte eine Ganzzahl sein! Bitte erneut eingeben...')

    sql = "DELETE FROM fahrer WHERE ID_Fahrer = %s"
    givID = (FHR_UserChoice,)
    srccursor.execute(sql, givID)
    verbindung.commit()

def deleteFahrzeug():

    print("\n### Fahrzeug löschen ###")

    getVehicles()

    while True:
        try:
            FZG_UserChoice = str(input("\n>>> Geben Sie das Kennzeichen des zu löschenden Fahrzeugs an: "))
            break
        except:
            print('\n Bitte geben Sie ein gültiges Kennzeichen ein!')

    sql = "DELETE FROM fahrzeug WHERE ID_Kennzeichen = %s"
    givID = (FZG_UserChoice,)
    srccursor.execute(sql, givID)
    verbindung.commit()

'''Programm'''

while state == 1:

    print(usermessage)

    while True:
        try:
            uservalue = int(input('\nIhre Eingabe: '))
            break
        except:
            print('Ihre Eingabe muss eine Ganzzahl sein!')

    if uservalue == 1:
        getFahrer()

    if uservalue == 2:
        createFahrer()

    if uservalue == 3:
        getVehicles()

    if uservalue == 4:
        createFahrzeug()

    if uservalue == 5:
        deleteFahrer()

    if uservalue == 6:
        deleteFahrzeug()

    if uservalue == 7:
        state = 0

    if uservalue not in allowedFeatures:
        print(">>> Aktuell werden nur die Funktionen 1 bis 6 unterstützt!")
        continue