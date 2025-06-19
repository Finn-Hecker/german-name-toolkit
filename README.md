# German Name Toolkit

Eine Sammlung von Python-Skripten zur Verwaltung und zum Auffinden deutscher Vornamen in Texten. Dieses Toolkit basiert auf einer umfangreichen Liste von Vornamen und nutzt den Aho-Corasick-Algorithmus für eine performante Suche.

## Features

-   **Effiziente Namenssuche:** `name_finder.py` findet Vornamen in einem gegebenen Text und gibt die gefundenen Namen sowie deren Position zurück. Die Implementierung nutzt einen Aho-Corasick-Automaten, um auch bei großen Texten und vielen Suchbegriffen eine hohe Performance zu gewährleisten.
-   **Datenmanagement:** Mit `name_add.py` können neue Namen einfach und sicher zur zentralen Namensliste (`vornamen.txt`) hinzugefügt werden. Das Skript prüft dabei automatisch auf bereits vorhandene Einträge.
-   **Datenbereinigung:** `name_eraser.py` sorgt für die Integrität der Daten, indem es exakte Duplikate aus der Namensliste entfernt.
-   **Umfangreiche Namensliste:** Die mitgelieferte `vornamen.txt` enthält bereits eine große Sammlung deutscher und in Deutschland gebräuchlicher Vornamen.

## Voraussetzungen

-   Python 3.x

Es sind keine externen Bibliotheken erforderlich.

## Setup

1.  Klone das Repository auf Deinen lokalen Rechner:
    ```bash
    git clone https://github.com/Finn-Hecker/german-name-toolkit.git
    ```

2.  Wechsle in das Verzeichnis des Projekts:
    ```bash
    cd german-name-toolkit
    ```

Alle Skripte sind direkt aus der Kommandozeile ausführbar. Die Datei `vornamen.txt` muss sich im selben Verzeichnis wie die Skripte befinden.

## Anwendung

Die folgenden Beispiele zeigen die Verwendung der einzelnen Skripte über die Kommandozeile.

### 1. Namen in einem Text finden (`name_finder.py`)

Dieses Skript durchsucht einen übergebenen Text nach Vornamen aus der `vornamen.txt`.

**Verwendung:**
```bash
python name_finder.py "Ein Text, in dem Peter und Anna vorkommen, aber auch Finn."
```

**Beispiel-Ausgabe:**
```
Gefundene Vornamen: 3
- Peter (Position: 20)
- Anna (Position: 32)
- Finn (Position: 53)
```

### 2. Neue Namen hinzufügen (`name_add.py`)

Fügt einen oder mehrere Namen zur `vornamen.txt` hinzu. Die Namen sollten durch Kommas getrennt sein.

**Verwendung (einzelner Name):**
```bash
python name_add.py David
```

**Verwendung (mehrere Namen):**
```bash
python name_add.py "Julia, Moritz, Clara"
```

**Beispiel-Ausgabe:**
```
Versuche 3 Namen hinzuzufügen...
Namen: Julia, Moritz, Clara

2 Namen hinzugefügt:
   + Julia
   + Moritz
1 Namen bereits vorhanden:
   - Clara
Gesamtanzahl Namen in 'vornamen.txt': 2584
```

### 3. Duplikate entfernen (`name_eraser.py`)

Dieses Skript liest die `vornamen.txt`, entfernt alle doppelten Einträge und speichert die bereinigte Liste zurück in die Datei.

**Verwendung:**
```bash
python name_eraser.py
```

**Beispiel-Ausgabe:**
```
Starte Duplikat-Entfernung...
Gelesene Namen aus 'vornamen.txt': 2585
Nach Bereinigung: 2582 Namen
Entfernte Duplikate: 3
Datei 'vornamen.txt' wurde aktualisiert!
Gefundene Duplikate: Max, Anna, Tom
Fertig!
```

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Details findest Du in der `LICENSE`-Datei.
