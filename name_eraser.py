#!/usr/bin/env python3

import os

def remove_duplicates_from_file():
    """
    Liest vornamen.txt, entfernt exakte Duplikate und überschreibt die Datei
    """
    filename = 'vornamen.txt'
    
    # Prüfen ob Datei existiert
    if not os.path.exists(filename):
        print(f"Datei '{filename}' nicht gefunden!")
        print("Bitte erstelle eine 'vornamen.txt' Datei im selben Verzeichnis.")
        return
    
    try:
        # Namen aus Datei lesen
        with open(filename, 'r', encoding='utf-8') as f:
            namen = [line.strip() for line in f if line.strip()]
        
        ursprüngliche_anzahl = len(namen)
        print(f"Gelesene Namen aus '{filename}': {ursprüngliche_anzahl}")
        
        # Duplikate entfernen mit dict.fromkeys()
        bereinigte_namen = list(dict.fromkeys(namen))
        
        neue_anzahl = len(bereinigte_namen)
        entfernte_duplikate = ursprüngliche_anzahl - neue_anzahl
        
        # Ergebnisse anzeigen
        print(f"Nach Bereinigung: {neue_anzahl} Namen")
        print(f"Entfernte Duplikate: {entfernte_duplikate}")
        
        if entfernte_duplikate > 0:
            # Datei mit bereinigter Liste überschreiben
            with open(filename, 'w', encoding='utf-8') as f:
                for name in bereinigte_namen:
                    f.write(name + '\n')
            
            print(f"Datei '{filename}' wurde aktualisiert!")
            
            # Zeige welche Namen mehrfach vorkamen
            duplikate = []
            gesehen = set()
            for name in namen:
                if name in gesehen and name not in duplikate:
                    duplikate.append(name)
                gesehen.add(name)
            
            if duplikate:
                print(f"Gefundene Duplikate: {', '.join(duplikate)}")
        else:
            print("Keine Duplikate gefunden - Datei bleibt unverändert.")
            
    except Exception as e:
        print(f"Fehler beim Verarbeiten der Datei: {e}")

if __name__ == "__main__":
    print("Starte Duplikat-Entfernung...")
    remove_duplicates_from_file()
    print("Fertig!")