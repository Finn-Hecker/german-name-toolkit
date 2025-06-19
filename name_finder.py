#!/usr/bin/env python3
"""
Verwendung: python name_finder.py <TEXT>
"""

import sys
import re
from typing import Set, List, Tuple
from collections import defaultdict


class AhoCorasickNameFinder:
    """Implementierung mit Aho-Corasick Algorithmus"""
    
    def __init__(self):
        self.names = set()
        self.trie = {}
        self.fail = {}
        self.output = defaultdict(list)
        self._load_and_build('vornamen.txt')
    
    def _load_and_build(self, filename: str):
        """Lädt Namen und baut Aho-Corasick Automaton"""
        # Lade Namen
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line in f:
                    name = line.strip()
                    if name:
                        self.names.add(name)
                        self.names.add(name.lower())
        except FileNotFoundError:
            print(f"Fehler: Datei '{filename}' nicht gefunden!")
            sys.exit(1)
        
        # Baue Trie
        for name in self.names:
            self._add_to_trie(name)
        
        # Baue Failure-Links
        self._build_failure_links()
    
    def _add_to_trie(self, word: str):
        """Fügt ein Wort zum Trie hinzu"""
        node = self.trie
        for char in word.lower():
            if char not in node:
                node[char] = {}
            node = node[char]
        node['$'] = word  # Markiere Wortende mit Original-Schreibweise
    
    def _build_failure_links(self):
        """Baut Failure-Links für Aho-Corasick"""
        from collections import deque
        
        queue = deque()
        # Initialisiere erste Ebene
        for char in self.trie:
            if char != '$':
                self.fail[id(self.trie[char])] = self.trie
                queue.append(self.trie[char])
        
        # BFS für weitere Ebenen
        while queue:
            current = queue.popleft()
            for char, child in current.items():
                if char == '$':
                    continue
                queue.append(child)
                
                # Finde Failure-Link
                fail_node = self.fail.get(id(current), self.trie)
                while fail_node != self.trie and char not in fail_node:
                    fail_node = self.fail.get(id(fail_node), self.trie)
                
                if char in fail_node and fail_node[char] != child:
                    self.fail[id(child)] = fail_node[char]
                else:
                    self.fail[id(child)] = self.trie
    
    def find_names(self, text: str) -> List[Tuple[str, int]]:
        """Findet alle Vornamen im Text mit Aho-Corasick"""
        results = []
        node = self.trie
        
        for i, char in enumerate(text):
            char_lower = char.lower()
            
            # Folge Failure-Links bis Match gefunden
            while node != self.trie and char_lower not in node:
                node = self.fail.get(id(node), self.trie)
            
            if char_lower in node:
                node = node[char_lower]
                
                # Prüfe auf vollständige Wörter
                temp = node
                while temp != self.trie:
                    if '$' in temp:
                        word_original = temp['$']
                        # Finde die tatsächliche Schreibweise im Text
                        start = i - len(word_original) + 1
                        if self._is_word_boundary(text, start, i + 1):
                            actual_word = text[start:i+1]
                            results.append((actual_word, start))
                    temp = self.fail.get(id(temp), self.trie)
        
        # Entferne Duplikate und sortiere nach Position
        unique_results = list(set(results))
        unique_results.sort(key=lambda x: x[1])
        
        return unique_results
    
    def _is_word_boundary(self, text: str, start: int, end: int) -> bool:
        """Prüft ob der gefundene Name an Wortgrenzen steht"""
        # Prüfe linke Grenze
        if start > 0 and text[start-1].isalnum():
            return False
        # Prüfe rechte Grenze
        if end < len(text) and text[end].isalnum():
            return False
        return True


def main():
    """Hauptprogramm"""
    # Prüfe Argumente
    if len(sys.argv) < 2:
        print("Verwendung: python name_finder.py <TEXT>")
        print("Beispiel: python name_finder.py \"Hallo Anna und Max, wie geht es euch?\"")
        sys.exit(1)
    
    # Text aus Argumenten
    text = ' '.join(sys.argv[1:])
    
    # Erstelle Finder und suche Namen
    finder = AhoCorasickNameFinder()
    results = finder.find_names(text)
    
    # Ausgabe
    if results:
        print(f"Gefundene Vornamen: {len(results)}")
        for name, pos in results:
            print(f"- {name} (Position: {pos})")
    else:
        print("Keine Vornamen gefunden.")


if __name__ == "__main__":
    main()