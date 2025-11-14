# Data Exploration mit uv

Diese Anleitung beschreibt Schritt für Schritt, wie mit `uv` ein neues Projekt erstellt und mit den nötigen Bibliotheken ausgestattet wird. 

## Voraussetzungen

- `uv` ist installiert.

## Schritt-für-Schritt-Anleitung

1. **Projekt initialisieren**  
   Im gewünschten Verzeichnis im Terminal oder GitBash den folgenden Befehl ausführen, um ein neues Projekt mit Python 3.11 zu erzeugen:

   ```bash
   uv init data-exploration --python 3.11
   ```

2. **Projektordner betreten**  
   Anschließend in den frisch angelegten Ordner wechseln:

   ```bash
   cd data-exploration
   ```

3. **Pakete installieren**  
   Nun die benötigten Bibliotheken hinzufügen:

   ```bash
   uv add pandas altair ipython jupyter
   ```

Nach diesen Schritten ist das Grundgerüst fertig eingerichtet. 

Nun kann VS Code gestartet werden:

```bash
uv code .
```

Alternativ kann VS Code auch manuell geöffnet und der Projektordner geladen werden.

## Umgebung testen

Im VS Code Terminal kann die Umgebung getestet werden. 

Das integrierte Terminal öffnen. 

```bash
uv run python main.py
```   

