#!/usr/bin/env python3

import sys
import os

def add_names_to_file(neue_namen):
    """
    Fügt neue Namen zur vornamen.txt hinzu, wenn sie noch nicht existieren.
    """
    filename = 'vornamen.txt'
    
    # Prüfen ob Datei existiert, wenn nicht erstellen
    if not os.path.exists(filename):
        print(f"Datei '{filename}' nicht gefunden - wird erstellt...")
        existierende_namen = []
    else:
        # Existierende Namen laden
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                existierende_namen = [line.strip() for line in f if line.strip()]
        except Exception as e:
            print(f"❌ Fehler beim Lesen der Datei: {e}")
            return
    
    existierende_namen_set = set(existierende_namen)
    
    # Namen verarbeiten
    hinzugefügte_namen = []
    bereits_vorhanden = []
    
    for name in neue_namen:
        name = name.strip()  # Leerzeichen entfernen
        
        if not name:  # Leere Namen ignorieren
            continue
            
        if name in existierende_namen_set:
            bereits_vorhanden.append(name)
        else:
            hinzugefügte_namen.append(name)
            existierende_namen_set.add(name)  # Für weitere Duplikat-Checks
    
    # Neue Namen zur Datei hinzufügen
    if hinzugefügte_namen:
        try:
            with open(filename, 'a', encoding='utf-8') as f:
                for name in hinzugefügte_namen:
                    f.write(name + '\n')
            
            print(f"{len(hinzugefügte_namen)} Namen hinzugefügt:")
            for name in hinzugefügte_namen:
                print(f"   + {name}")
                
        except Exception as e:
            print(f"Fehler beim Schreiben in die Datei: {e}")
            return
    
    # Bereits vorhandene Namen anzeigen
    if bereits_vorhanden:
        print(f"{len(bereits_vorhanden)} Namen bereits vorhanden:")
        for name in bereits_vorhanden:
            print(f"   - {name}")
    
    # Zusammenfassung
    if hinzugefügte_namen:
        aktuelle_anzahl = len(existierende_namen) + len(hinzugefügte_namen)
        print(f"Gesamtanzahl Namen in '{filename}': {aktuelle_anzahl}")
    elif bereits_vorhanden:
        print("Keine neuen Namen hinzugefügt.")
    else:
        print("Keine gültigen Namen angegeben.")

def main():
    """
    Hauptfunktion - verarbeitet Kommandozeilenargumente
    """
    if len(sys.argv) < 2:
        print("   Verwendung: python name_add.py <Name1,Name2,Name3>")
        print("   Beispiele:")
        print("   python name_add.py Finn")
        print("   python name_add.py Finn,Jonas,Leon")
        return
    
    # Alle Argumente zusammenfügen
    eingabe = ' '.join(sys.argv[1:])
    
    # Namen nach Komma trennen
    namen_liste = [name.strip() for name in eingabe.split(',')]
    
    print(f"Versuche {len(namen_liste)} Namen hinzuzufügen...")
    print(f"Namen: {', '.join(namen_liste)}")
    print()
    
    add_names_to_file(namen_liste)

if __name__ == "__main__":
    main()