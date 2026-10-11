# Session 1 Onboarding Tutorial Data Vizualization & Data Story Telling: Python, IDE und Version Control mit Git(Hub) 

### Lernziele

Nach diesem Tutorial sind Sie bereit für die Aufgaben und die Prüfung im Kurs Data Vizualization & Data Story Telling:

- eine Python-Umgebung für die Veranstaltung einrichten,
- Jupyter Notebooks in **VS Code** oder **Google Colab** ausführen,
- mit `pandas` und `matplotlib` ein erstes Data-Science-Beispiel bearbeiten,
- ein eigenes **GitHub-Repository** anlegen,
- Änderungen mit **Git** versionieren,
- mit den wichtigsten Git-Befehlen arbeiten.

> **Ziel:** Durchlaufen Sie das Tutorial (30–45 Minuten) bis kommende Woche, so dass Sie Sie technisch startklar für die Übungen der Veranstaltung und Ihre Projektarbeit sind.

---

## 1. Welche Variante soll ich verwenden?

Für die Veranstaltung empfehlen wir zwei Möglichkeiten um mit einer Standard IDE () + Versionskontrolle Data Science Aufgaben zu bearbeiten. Welche Variante Sie wählen, bleibt Ihnen überlassen.  

### Variante A: VS Code (OnPremise) + Anaconda

Diese Variante eignet sich besonders, wenn Sie:

- regelmäßig mit Python arbeiten möchten,
- Dateien lokal speichern wollen,
- Git und GitHub verwenden,
- später größere Projekte bearbeiten möchten.

### Alternative Variante B: Google Colab (Cloud)

Google Colab eignet sich besonders, wenn:

- die lokale Installation nicht funktioniert,
- Sie sofort starten möchten,
- Sie nur einen Browser zur Verfügung haben.

| | VS Code + Anaconda | Google Colab |
|---|---|---|
| Installation nötig | Ja | Nein |
| Offline nutzbar | Ja | Nein |
| Dateien lokal | Ja | Eingeschränkt |
| Git/GitHub-Workflow | Sehr gut | Eingeschränkt |
| Für größere Projekte | Sehr gut | Bedingt |
| Empfehlung | **Standard im Kurs** | **Fallback Lösung** |

Für die Veranstaltung verwenden wir **Jupyter Notebooks (`.ipynb`)**. Dieses Format funktioniert in beiden Umgebungen.

---

## 2. Variante A: VS Code + Anaconda

### 2.1 Anaconda installieren

Installieren Sie die **Anaconda Distribution**:

https://www.anaconda.com/download

Anaconda bringt unter anderem mit:

- Python
- den Paketmanager `conda`
- Jupyter
- Werkzeuge zur Verwaltung von Python-Umgebungen

#### Installation prüfen

Unter Windows:

**Anaconda Prompt** öffnen.

Unter macOS/Linux:

**Terminal** öffnen.

Dann:

```bash
conda --version
```

Wenn eine Versionsnummer erscheint, funktioniert die Installation.

Beispiel:

```text
conda 25.x.x
```

---

## 3. Microsoft VS Code installieren

Download:

https://code.visualstudio.com/

Nach der Installation öffnen Sie in VS Code den Bereich:

**Extensions**

Installieren Sie mindestens:

- **Python** von Microsoft
- **Jupyter** von Microsoft

---

## 4. Warum verwenden wir eine eigene Python-Umgebung?

Python-Projekte verwenden oft unterschiedliche Bibliotheken und Versionen.

Damit sich verschiedene Projekte nicht gegenseitig beeinflussen, legen wir für diese Veranstaltung eine eigene Umgebung an.

Wir nennen sie:

```text
dataviz
```

### Umgebung erstellen

Öffnen Sie den **Anaconda Prompt**:

```bash
conda create -n dataviz python=3.12
```

Bestätigen Sie die Installation gegebenenfalls mit:

```text
y
```

Danach aktivieren:

```bash
conda activate dataviz
```

Sie sollten nun im Terminal ungefähr Folgendes sehen:

```text
(dataviz) C:\...
```

Das zeigt, dass die Umgebung aktiv ist.

---

## 5. Benötigte Bibliotheken installieren

Installieren Sie die wichtigsten Data-Science-Pakete:

```bash
conda install pandas numpy matplotlib seaborn jupyter ipykernel
```

Diese Bibliotheken benötigen wir regelmäßig:

| Bibliothek | Zweck |
|---|---|
| `pandas` | Daten einlesen und bearbeiten |
| `numpy` | numerische Berechnungen |
| `matplotlib` | Visualisierung |
| `seaborn` | statistische Visualisierung |
| `jupyter` | Jupyter Notebooks |
| `ipykernel` | Python-Kernel für Notebooks |


Empfohlene VS Code Extensions 

# Übersicht

| Erweiterung | Zweck | Empfehlung | Open Source / Lizenz | Installation im Terminal |
|---|---|---:|---|---|
| **Python** – Microsoft | Python-Unterstützung in VS Code: Interpreter-Auswahl, Debugging, Navigation, Refactoring und Integration weiterer Python-Tools | Pflicht | Ja, MIT | `code --install-extension ms-python.python` |
| **Jupyter** – Microsoft | Öffnen und Ausführen von `.ipynb`-Notebooks direkt in VS Code; Kernel-Auswahl, Zellen, Outputs und Visualisierungen | Pflicht | Ja, MIT | `code --install-extension ms-toolsai.jupyter` |
| **Rainbow CSV** – mechatroner | Färbt CSV-/TSV-Spalten unterschiedlich ein, erkennt Trennzeichen und erleichtert das Lesen großer Texttabellen | Empfehlung | Ja, MIT | `code --install-extension mechatroner.rainbow-csv` |
| **Ruff** – Astral | Sehr schneller Python-Linter und Formatter; findet typische Fehler, unbenutzte Imports und Style-Probleme | Empfehlung | Ja, MIT | `code --install-extension charliermarsh.ruff` |
| **Data Wrangler** – Microsoft | Grafische Exploration und Transformation von DataFrames; kann pandas-Code für Transformationen erzeugen | Empfehlung | **Nein – Microsoft-Lizenz** | `code --install-extension ms-toolsai.datawrangler` |
| **Edit CSV** – janisdd | Öffnet CSV-Dateien in einer Excel-artigen Tabellenansicht und erlaubt direktes Editieren | Optional | Ja, MIT | `code --install-extension janisdd.vscode-edit-csv` |
| **Data Preview** – Random Fractals | Interaktive Vorschau für u. a. JSON, YAML, Parquet, Arrow und Excel; bietet auch einfache Charting-Funktionen | Optional | Ja, Apache-2.0 | Über Extensions suchen: `Data Preview` |
| **Quarto** | Wissenschaftliche und technische Dokumente mit Markdown, Python und reproduzierbaren Ausgaben; geeignet für Reports und Data Storytelling | Optional | Ja, MIT (VS-Code-Erweiterung) | Über Extensions suchen: `Quarto` |

#### Installation über die VS-Code-Oberfläche

Alternativ können alle Erweiterungen grafisch installiert werden.

**Schritt 1**

VS Code öffnen.

**Schritt 2**

Links auf das Symbol:

```text
Extensions
```

klicken.

Tastenkürzel:

```text
Ctrl + Shift + X
```

**Schritt 3**

Nach dem Namen der Erweiterung suchen, z. B.:

```text
Rainbow CSV
```

**Schritt 4**

Auf den **Publisher** achten.

Beispielsweise:

```text
Rainbow CSV
Publisher: mechatroner
```

**Schritt 5**

Auf:

```text
Install
```

klicken.

**Installation kontrollieren**

Öffnen Sie:

```text
Extensions → Installed
```

---

## 6. Projektordner anlegen

Legen Sie einen Ordner für die Veranstaltung an.

Beispiel:

```text
data-science/
├── data/
├── notebooks/
└── README.md
```

Öffnen Sie den Ordner in VS Code:

**File → Open Folder**

Warum diese Struktur?

- `data/` enthält Datensätze.
- `notebooks/` enthält Analysen und Übungen.
- `README.md` beschreibt das Projekt.

---

## 7. Erstes Jupyter Notebook

Erstellen Sie im Ordner `notebooks` eine Datei:

```text
01_hello_data_science.ipynb
```

Oben rechts in VS Code finden Sie:

**Select Kernel**

Wählen Sie:

```text
Python Environments → dataviz
```

### Was ist ein Kernel?

Ein Kernel ist die Python-Umgebung, in der der Code eines Notebooks ausgeführt wird.

Wenn der falsche Kernel ausgewählt ist, kann es passieren, dass Python eine Bibliothek nicht findet, obwohl Sie sie installiert haben.

---

## 8. Wie funktioniert ein Jupyter Notebook?

Ein Notebook besteht aus **Zellen**.

Es gibt hauptsächlich zwei Typen:

### Markdown-Zellen

Für:

- Überschriften
- Erklärungen
- Dokumentation
- Formeln

### Code-Zellen

Für Python-Code.

Eine Zelle führen Sie mit:

```text
Shift + Enter
```

aus.

---

## 9. Ihr erstes Python-Beispiel

Führen Sie folgende Code-Zelle aus:

```python
print("Hello Data Science!")
```

Ausgabe:

```text
Hello Data Science!
```

Damit wissen Sie:

- der Kernel funktioniert,
- Python wird ausgeführt,
- Ihr Notebook ist einsatzbereit.

---

## 10. Erster Data-Science-Workflow

Ein typischer Data-Science-Workflow sieht vereinfacht so aus:

```text
Daten
  ↓
Daten einlesen
  ↓
Daten untersuchen
  ↓
Daten verändern
  ↓
Visualisieren
  ↓
Interpretieren
```

Wir spielen diesen Ablauf mit einem kleinen Beispiel durch.

---

## 11. Daten mit pandas erzeugen

```python
import pandas as pd

df = pd.DataFrame({
    "Jahr": [2020, 2021, 2022, 2023, 2024],
    "Umsatz": [100, 108, 105, 120, 135]
})

df
```

Die Variable `df` enthält einen **DataFrame**.

Ein DataFrame ist eine tabellarische Datenstruktur – vergleichbar mit einer Tabelle in Excel.

---

## 12. Daten untersuchen

Einige wichtige Befehle:

```python
df.head()
```

zeigt die ersten Zeilen.

```python
df.shape
```

zeigt:

```text
(Zeilen, Spalten)
```

```python
df.columns
```

zeigt die Spaltennamen.

```python
df.describe()
```

liefert statistische Kennzahlen.

Probieren Sie die Befehle aus.

---

## 13. Erste Visualisierung mit der Bibliothek matplotlib

```python
import matplotlib.pyplot as plt

plt.plot(df["Jahr"], df["Umsatz"], marker="o")

plt.xlabel("Jahr")
plt.ylabel("Umsatz")
plt.title("Umsatzentwicklung")

plt.show()
```

Sie haben damit bereits einen vollständigen kleinen Data-Science-Workflow durchgeführt:

```text
Daten
→ DataFrame
→ Exploration
→ Visualisierung
```

---

## 14. Mini-Aufgabe

Verändern Sie den Datensatz:

```python
df = pd.DataFrame({
    "Jahr": [2020, 2021, 2022, 2023, 2024],
    "Umsatz": [100, 108, 105, 120, 135]
})
```

### Aufgabe

1. Ergänzen Sie das Jahr **2025**.
2. Wählen Sie selbst einen Umsatzwert.
3. Führen Sie die Visualisierung erneut aus.
4. Ändern Sie den Titel der Grafik.

Ziel ist nicht die perfekte Grafik.

Ziel ist, dass Sie verstehen:

> **Notebook-Code kann interaktiv verändert und erneut ausgeführt werden.**

---

## 15. Installation testen

Führen Sie folgende Zelle aus:

```python
import sys
import numpy as np
import pandas as pd
import matplotlib
import seaborn as sns

print("Python:", sys.version)
print("NumPy:", np.__version__)
print("Pandas:", pd.__version__)
print("Matplotlib:", matplotlib.__version__)
print("Seaborn:", sns.__version__)

print("\n✓ Umgebung funktioniert!")
```

Wenn am Ende

```text
✓ Umgebung funktioniert!
```

erscheint, ist Ihre Umgebung einsatzbereit.

---

## 16. Alternative: Google Colab

Google Colab funktioniert vollständig im Browser.

Öffnen Sie:

https://colab.research.google.com/

### Vorgehen

1. Mit Google-Konto anmelden.
2. **New Notebook** auswählen.
3. Python-Code eingeben.
4. Zelle mit **Shift + Enter** ausführen.

Hinweis: Viele typische Data-Science-Bibliotheken sind bereits in der Standard Python Umgebung installiert und können direkt mit _import_ geladen werden. 

Beispiel:

```python
import pandas as pd
import matplotlib.pyplot as plt

print("Colab funktioniert!")
```

---

## 17. Wann sollte ich Colab verwenden?

Colab ist hilfreich, wenn:

- Ihre lokale Python-Installation Probleme macht,
- Sie schnell etwas ausprobieren möchten,
- Sie an einem fremden Rechner arbeiten.

Empfehlung:  

```text
GitHub
   ↕
Git
   ↕
VS Code
   ↕
Python / Jupyter
```

**Damit lernen Sie gleichzeitig einen Workflow kennen, der auch in vielen Unternehmen und Forschungsprojekten verwendet wird.**

---

## 18. Warum Versionskontrolle?

Stellen Sie sich folgende Dateien vor:

```text
analyse_final.ipynb
analyse_final2.ipynb
analyse_final_NEU.ipynb
analyse_final_NEU2.ipynb
analyse_final_WIRKLICH_FINAL.ipynb
```

Das ist keine gute Versionskontrolle. 
Git löst dieses Problem.

Mit Git können Sie:

- Änderungen im Code nachvollziehen,
- frühere Versionen wiederherstellen,
- gemeinsam an Projekten arbeiten,
- Ihren Code auf GitHub online sichern.

---

## 19. Git und GitHub

Die Begriffe werden häufig verwechselt. Die Unterschiede zu kennen ist wichtig. 

### Git

Git ist ein Programm für **Versionskontrolle**.

Git läuft auf Ihrem Rechner.

### GitHub

GitHub ist eine Plattform im Internet, auf der Git-Projekte gespeichert werden können.

### Repository

Ein Repository – kurz **Repo** – ist ein Projektordner mit Versionshistorie.

Vereinfacht:

```text
Git       = Versionskontrolle
GitHub    = Plattform für Git-Repositories
Repository = Projekt
```

---

## 20. GitHub-Konto erstellen

Falls noch nicht vorhanden:

https://github.com/

Erstellen Sie dort einen Account.

> **Wichtig:** Speichern Sie niemals Passwörter, API-Keys, Tokens oder vertrauliche Daten in einem öffentlichen Repository. Achten Sie darauf, dass Sie in .gitignore Ausnahmen für z.B. lokale .env Files oder auch Datensätze explizit aufnehmen. Sie können bspw. einzelene Datein, Dateitypen oder Ordner von der Überwachung durch git ausnehmen.  

---

## 21. Git (SCM, Source Code Management) installieren

Download:

https://git-scm.com/downloads 

Anschließend VS Code gegebenenfalls neu starten.

Prüfen Sie im Terminal:

```bash
git --version
```

Wenn eine Versionsnummer erscheint, funktioniert Git.

---

## 22. Git einmalig konfigurieren

Git speichert bei jeder Version, wer die Änderung vorgenommen hat.

Einmalig ausführen:

```bash
git config --global user.name "Vorname Nachname"
```

und:

```bash
git config --global user.email "ihre-email@example.com"
```

Kontrolle:

```bash
git config --global --list
```

---

## 23. Eigenes GitHub-Repository erstellen

Auf GitHub:

1. Rechts oben auf **+**
2. **New repository**
3. Namen vergeben, z. B.

```text
data-science-course
```

4. **Public** oder **Private** auswählen
5. **Add a README file** aktivieren
6. **Create repository**

---

## 24. Repository auf den Rechner holen

Dafür verwenden wir:

```bash
git clone
```

Kopieren Sie auf GitHub die HTTPS-Adresse des Repositories.

Beispiel:

```bash
git clone https://github.com/USERNAME/data-science-course.git
```

Danach in den Ordner wechseln:

```bash
cd data-science-course
```

Diesen Ordner anschließend in VS Code öffnen.

### Merksatz

```text
git clone
```

brauchen Sie normalerweise nur **einmal**, wenn Sie ein Repository erstmals auf Ihren Rechner holen.

---

## 25. Der wichtigste Git-Befehl

Wenn Sie nicht wissen, was gerade passiert:

```bash
git status
```

`git status` zeigt unter anderem:

- neue Dateien,
- veränderte Dateien,
- Dateien, die für einen Commit vorbereitet sind.

Führen Sie diesen Befehl häufig aus.

---

## 26. Der zentrale Git-Workflow

Die wichtigsten Schritte sind:

```text
Datei bearbeiten
     ↓
git status
     ↓
git add
     ↓
git commit
     ↓
git push
```

Wir gehen diese Schritte nun einzeln durch: 

---

### 26.1 Schritt 1: Änderungen ansehen

```bash
git status
```

Beispielsweise könnte Git anzeigen:

```text
modified: notebooks/01_analysis.ipynb
```

Das bedeutet:

Die Datei wurde seit dem letzten gespeicherten Stand verändert.

---

### 26.2 Schritt 2: Änderungen auswählen

Eine bestimmte Datei:

```bash
git add notebooks/01_analysis.ipynb
```

Alle Änderungen:

```bash
git add .
```

Wichtig:

`git add` speichert noch keine neue Version.

Es bedeutet:

> Diese Änderungen sollen Teil des nächsten Commits werden.

---

### 26.3 Schritt 3: Commit erstellen

```bash
git commit -m "Add first visualization"
```

Ein Commit ist ein gespeicherter Stand Ihres Projekts.

Die Commit-Nachricht beschreibt die Änderung.

#### Gute Beispiele

```text
Add income visualization
Fix axis labels
Add exercise 2
Update data cleaning
```

#### Weniger gute Beispiele

```text
test
neu
changes
final final
asdf
```

Eine gute Commit-Nachricht beantwortet:

> Was wurde geändert?

---

### 26.4 Schritt 4: Änderungen zu GitHub übertragen

```bash
git push
```

Damit werden Ihre lokalen Commits zu GitHub übertragen.

Prüfen Sie anschließend Ihr Repository im Browser.

Ihre Änderungen sollten dort sichtbar sein.

---

### 26.5 Änderungen von GitHub holen

Wenn sich das Repository auf GitHub geändert hat:

```bash
git pull
```

Ein sinnvoller Beginn einer Arbeitssitzung ist deshalb häufig:

```bash
git pull
```

Damit holen Sie zuerst den aktuellen Stand.

---

### 26.6 Der typische Workflow

Am Anfang:

```bash
git pull
```

Dann arbeiten Sie an Ihren Dateien.

Anschließend:

```bash
git status
git add .
git commit -m "Add exercise solution"
git push
```

Diese wenigen Befehle reichen für den Einstieg bereits aus.

---

### 26.7 Mini-Übung: Ihr erster Git-Commit

Erstellen Sie in Ihrem Repository eine Datei:

```text
hello.py
```

Inhalt:

```python
print("Hello GitHub!")
```

Speichern Sie die Datei.

Dann:

```bash
git status
```

Sie sollten sehen, dass `hello.py` noch nicht versioniert ist.

Nun:

```bash
git add hello.py
```

Noch einmal:

```bash
git status
```

Jetzt ist die Datei für den Commit vorbereitet.

Commit erstellen:

```bash
git commit -m "Add hello example"
```

Zu GitHub übertragen:

```bash
git push
```

Öffnen Sie anschließend Ihr Repository im Browser.

Wenn `hello.py` dort erscheint, haben Sie erfolgreich:

```text
lokale Datei
→ Git
→ Commit
→ GitHub
```

durchlaufen.

---

## 27. Git direkt in VS Code

VS Code bietet eine grafische Oberfläche für Git.

Links finden Sie:

**Source Control**

Dort sehen Sie:

- geänderte Dateien,
- Unterschiede zwischen Versionen,
- vorbereitete Änderungen,
- Commit-Feld,
- Synchronisierung mit GitHub.

Für den Einstieg dürfen Sie diese Oberfläche gerne verwenden.

Trotzdem sollten Sie diese Befehle kennen:

```bash
git status
git add
git commit
git pull
git push
```

Sie helfen Ihnen zu verstehen, was im Hintergrund passiert.

---

## 28. GitHub und Google Colab

Auch Google Colab kann mit GitHub zusammenarbeiten.

Sie können beispielsweise:

- ein Notebook aus GitHub in Colab öffnen,
- ein Colab-Notebook wieder auf GitHub speichern.

Für das Erlernen von Versionskontrolle ist jedoch der lokale Workflow übersichtlicher:

```text
GitHub
   ↑ ↓
 Git
   ↑ ↓
VS Code
```

---

## 29. Was Sie zunächst noch nicht brauchen

Git kann sehr viel mehr.

Begriffe wie

```text
branch
merge
rebase
pull request
cherry-pick
```

werden später wichtig.

Für den Einstieg reichen jedoch:

```bash
git clone
git status
git add
git commit
git pull
git push
```

---

## 30. Git-Spickzettel

| Befehl | Bedeutung |
|---|---|
| `git clone URL` | Repository erstmals herunterladen |
| `git status` | Aktuellen Zustand anzeigen |
| `git add DATEI` | Datei für Commit auswählen |
| `git add .` | Alle Änderungen auswählen |
| `git commit -m "..."` | Version lokal speichern |
| `git push` | Commits zu GitHub übertragen |
| `git pull` | Änderungen von GitHub holen |
| `git log --oneline` | Commit-Historie anzeigen |

---

## 31. Fehlersuche

### Python findet ein Paket nicht

Beispiel:

```text
ModuleNotFoundError
```

Prüfen Sie zuerst den Kernel.

In VS Code:

```text
Select Kernel → dataviz
```

Falls das Paket tatsächlich fehlt:

```bash
conda activate dataviz
conda install paketname
```

---

### `conda` wird nicht gefunden

Unter Windows verwenden Sie zunächst den:

```text
Anaconda Prompt
```

Statt PowerShell oder CMD.

---

### Git zeigt sehr viele unbekannte Dateien

Führen Sie aus:

```bash
git status
```

und prüfen Sie zunächst, welche Dateien Git gefunden hat.

Nicht blind:

```bash
git add .
```

ausführen, wenn Sie nicht wissen, welche Dateien dadurch aufgenommen werden.

---

### `git push` funktioniert nicht

Häufige Ursachen:

- keine Internetverbindung,
- Anmeldung bei GitHub fehlt,
- Remote-Repository ist nicht korrekt eingerichtet,
- lokales Repository ist nicht aktuell.

Prüfen Sie zunächst:

```bash
git status
```

und anschließend:

```bash
git pull
```

---

## 33. Abschluss-Check

Sie sind startklar, wenn Sie alle Punkte beantworten können:

- [ ] Kann ich VS Code starten?
- [ ] Ist die Conda-Umgebung `dataviz` vorhanden?
- [ ] Kann ich ein `.ipynb`-Notebook öffnen?
- [ ] Ist der Kernel `dataviz` ausgewählt?
- [ ] Kann ich eine Python-Zelle ausführen?
- [ ] Kann ich einen `pandas`-DataFrame erzeugen?
- [ ] Kann ich eine einfache Grafik erzeugen?
- [ ] Habe ich einen GitHub-Account?
- [ ] Habe ich ein eigenes Repository?
- [ ] Kann ich `git status` ausführen?
- [ ] Kann ich Änderungen committen?
- [ ] Kann ich Änderungen mit `git push` zu GitHub übertragen?

Wenn diese Punkte funktionieren, ist Ihr Setup für die Übungen einsatzbereit.

---

## 34. Die wichtigsten Befehle auf einen Blick

### Python-Umgebung

```bash
conda activate dataviz
```

### Notebook

```text
Shift + Enter
```

### Git

```bash
git pull
git status
git add .
git commit -m "Beschreibung"
git push
```

### Wichtigster Tipp

Wenn etwas mit Git unklar ist:

```bash
git status
```

Wenn etwas mit Python-Paketen unklar ist:

> Prüfen Sie zuerst, ob der richtige **Kernel** ausgewählt ist.

---

### 35 ENDLICH GESCHAFFT 🎉

Sie haben jetzt die technische Grundlage für die Veranstaltung eingerichtet:

```text
Python
+
Jupyter
+
VS Code
+
Git
+
GitHub
```

Im nächsten Schritt können wir uns auf das konzentrieren, worum es eigentlich geht:

**Daten analysieren, visualisieren und verständlich kommunizieren.** 
