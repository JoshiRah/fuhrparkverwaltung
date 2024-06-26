'''Module'''
import datetime
import time

import mysql.connector

'''DB Verbindung'''

while True:
    try:
        verbindung = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="",
        database="fuhrpark"
        )
        break
    except:
        print("\n>>> ACHTUNG - ES KONNTE KEINE DATENBANK ERREICHT WERDEN! <<<")

srccursor = verbindung.cursor()


'''Globale Variablen'''

usermessage = "\n\n##################################\n| >>> Bitte wählen Sie ein Menü:\n##################################\n\n 1 - Fahrer anzeigen\n 2 - Fahrer anlegen\n 3 - Fahrzeuge anzeigen\n 4 - Fahrzeug anlegen\n 5 - Fahrer löschen\n 6 - Fahrzeug löschen\n 7 - Wartung anlegen\n 8 - Wartungen anzeigen\n 9 - Programm beenden"
uservalue = 0
allowedFeatures = [1,2,3,4,5,6,7,8,9]
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

def getFahrzeuge():
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

def deleteFahrzeug():

    print("\n### Fahrzeug löschen ###")

    getFahrzeuge()

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

def createWartung():
    print('\n### Wartung wird angelegt ### \n')
    fzg_ID = input("\nGeben Sie das Kennzeichen des Fahrzeuges an: ")
    datum = str(datetime.datetime.today()).split()[0]
    arbeiten = input("\nWelche Arbeiten wurden durchgeführt: ")

    while True:
        try:
            kosten = float(input("Kosten der Wartung: "))
            break
        except:
            print("\n> Die Kosten müssen als Fließkomma- bzw. Ganzzahl angegeben werden!\n")

    sql = "INSERT INTO wartung (Datum, Arbeiten, Kosten, ID_Kennzeichen) VALUES (%s, %s, %s, %s)"
    val = (datum, arbeiten, kosten, fzg_ID)
    srccursor.execute(sql, val)
    verbindung.commit()

def showWartungenByFahrzeug():
    counter = 1
    print("\n### Wartungen je Fahrzeug anzeigen###")
    getFahrzeuge()
    usr_FZG_value = (input("\n>>> Von welchem Fahrzeug möchten Sie die Wartungen sehen? "), )

    sql = "SELECT * FROM wartung WHERE ID_Kennzeichen = %s"
    srccursor.execute(sql, usr_FZG_value)

    wartungen = srccursor.fetchall()

    print("\n>>> Registrierte Wartungen für das Fahrzeug mit dem Kennzeichen ", usr_FZG_value)

    for wartung in wartungen:
        print("\n> Wartung Nr. ", counter)
        print("Datum der Wartung -> ", wartung[1])
        print("Durchgeführte Arbeiten -> ", wartung[2])
        print("Kosten der Wartung -> ", wartung[3])

        counter += 1

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
        while True:
            try:
                getFahrer()
                break
            except:
                print("\n>>> Achtung! Es ist ein Fehler aufgetreten. Prüfen Sie die Datenbankverbindung!")
                time.sleep(1)
                exit()

    if uservalue == 2:
        while True:
            try:
                createFahrer()
                break
            except:
                print("\n>>> Achtung! Es ist ein Fehler aufgetreten. Prüfen Sie die Datenbankverbindung!")
                time.sleep(1)
                exit()

    if uservalue == 3:
        while True:
            try:
                getFahrzeuge()
                break
            except:
                print("\n>>> Achtung! Es ist ein Fehler aufgetreten. Prüfen Sie die Datenbankverbindung!")
                time.sleep(1)
                exit()

    if uservalue == 4:
        while True:
            try:
                createFahrzeug()
                break
            except:
                print("\n>>> Achtung! Es ist ein Fehler aufgetreten. Prüfen Sie die Datenbankverbindung!")
                time.sleep(1)
                exit()

    if uservalue == 5:
        while True:
            try:
                deleteFahrer()
                break
            except:
                print("\n>>> Achtung! Es ist ein Fehler aufgetreten. Prüfen Sie die Datenbankverbindung!")
                time.sleep(1)
                exit()

    if uservalue == 6:
        while True:
            try:
                deleteFahrzeug()
                break
            except:
                print("\n>>> Achtung! Es ist ein Fehler aufgetreten. Prüfen Sie die Datenbankverbindung!")
                time.sleep(1)
                exit()

    if uservalue == 7:
        while True:
            try:
                createWartung()
                break
            except:
                print("\n>>> Achtung! Es ist ein Fehler aufgetreten. Prüfen Sie die Datenbankverbindung!")
                time.sleep(1)
                exit()

    if uservalue == 8:
        while True:
            try:
                showWartungenByFahrzeug()
                break
            except:
                print("\n>>> Achtung! Es ist ein Fehler aufgetreten. Prüfen Sie die Datenbankverbindung!")
                time.sleep(1)
                exit()

    if uservalue == 9:
        state = 0

    if uservalue not in allowedFeatures:
        print(">>> Aktuell werden nur die Funktionen ",min(allowedFeatures)," bis ", max(allowedFeatures), " unterstützt!")
        continue
