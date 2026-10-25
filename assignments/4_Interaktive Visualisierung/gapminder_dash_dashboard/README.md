# Lecture 4 Gapminder Explorer – ein Plotly-Dash-Beispiel

Dieses Beispiel zeigt, wie aus einem Plotly-Diagramm ein interaktives **Dashboard** wird. 
Die App verbindet hierfür einen Bubble Chart, ein Histogramm, Kennzahlen und einen Länder-Zeitverlauf. Jahr und Kontinent wirken als gemeinsame Filter; ein Klick auf einen Punkt öffnet die Detailansicht des Landes.

## Lernziele
Nach dem Durcharbeiten kannst du:

1. den Unterschied zwischen **Plotly** (Diagramme) und **Dash** (Webanwendung) erklären,
2. ein Dash-Layout aus Komponenten zusammensetzen,
3. mit Callbacks Eingaben (`Input`) und Ausgaben (`Output`) verbinden,
4. mehrere Visualisierungen konsistent aus einer gefilterten Datenbasis aktualisieren,
5. Klickdaten eines Diagramms für eine zweite Ansicht verwenden.

## Installation und Start

Öffne PowerShell (Windows) in diesem Ordner und führe aus, um ein virtuelles Environment zu erstellen:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Öffne anschließend die im Terminal angezeigte Localhost Adresse, normalerweise <http://127.0.0.1:8050>.

Falls im Repository bereits die übergeordnete virtuelle Umgebung aktiviert ist, genügen:

```powershell
python -m pip install -r requirements.txt
python app.py
```

## Die fünf Bausteine in Plotly Dash

### 1. Daten

```python
DF = px.data.gapminder()
```

Der Gapminder-Datensatz wird mit Plotly Express ausgeliefert. Jede Zeile beschreibt ein Land in einem Jahr. Wichtige Variablen sind `country`, `continent`, `year`, `lifeExp`, `pop` und `gdpPercap`.

### 2. Komponenten

Dash-Oberflächen bestehen aus Komponenten:

- `html.*` erzeugt HTML-Strukturen wie Überschriften, Abschnitte und Karten.
- `dcc.*` liefert interaktive Komponenten wie Slider, Dropdowns und Diagramme.

Jede Komponente, die ein Callback ansprechen soll, erhält eine eindeutige `id`, zum Beispiel `year-slider` oder `bubble-chart`.

### 3. Layout

`app.layout` beschreibt den Komponentenbaum der Seite. Das ist die **statische Struktur**: Wo stehen Filter, Texte und Diagramme? Das CSS in `assets/styles.css` gestaltet diese Struktur. Dash lädt Dateien im Ordner `assets` automatisch.

### 4. Figures

Plotly Express erzeugt Figure-Objekte. Ein Beispiel:

```python
figure = px.scatter(
    data,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    log_x=True,
)
```

Die Variablen werden auf visuelle Kanäle abgebildet:

| Datenvariable | Visueller Kanal |
|---|---|
| BIP pro Kopf | X-Position |
| Lebenserwartung | Y-Position |
| Bevölkerung | Punktfläche |
| Kontinent | Farbe |

Die logarithmische X-Achse ist wichtig, weil sich die BIP-Werte über mehrere Größenordnungen erstrecken.

### 5. Callbacks

Ein Callback macht die Seite reaktiv:

```python
@callback(
    Output("bubble-chart", "figure"),
    Input("year-slider", "value"),
)
def update_chart(year):
    data = DF[DF["year"] == year]
    return px.scatter(data, x="gdpPercap", y="lifeExp")
```

Das Prinzip lautet:

```text
Benutzeraktion → Input → Python-Funktion → Output → aktualisierte Oberfläche
```

In der Beispiel-App liefert `update_overview()` bewusst **mehrere Outputs**. So verwenden Kennzahlen, Bubble Chart und Histogramm exakt denselben Filterzustand. `update_country_history()` liest dagegen die `clickData` des Bubble Charts und demonstriert die Verknüpfung zweier Ansichten.

## Bezug zur Vorlesung und der Theorie: 

Das Dashboard folgt Ben Shneidermans Mantra:

1. **Overview first:** Kennzahlen und Bubble Chart geben einen Überblick.
2. **Zoom and filter:** Jahr, Kontinentfilter sowie Plotly-Zoom grenzen die Analyse ein.
3. **Details-on-demand:** Hover zeigt Werte; ein Klick öffnet die Länderhistorie.

Dabei gilt: **Interaktivität ist kein Selbstzweck**. Jede **Interaktion beantwortet eine konkrete Frage**. Filter reduzieren Komplexität, Hover hält die Darstellung ruhig und Klicks stellen einen Zusammenhang zwischen Überblick und Detail her.

## Code-Landkarte

| Bereich in `app.py` | Aufgabe |
|---|---|
| Konstanten und `filter_data()` | Daten und gemeinsame Filterlogik |
| `app.layout` | Aufbau der Benutzeroberfläche |
| `update_overview()` | koordinierte Aktualisierung der Übersichten |
| `update_country_history()` | Details nach einem Klick |
| `app.run()` | lokaler Entwicklungsserver |

## Bonus: Sinnvolle Lernaufgaben 

1. Ergänze einen **Schalter** für eine lineare/logarithmische X-Achse.
2. Füge eine **Weltkarte** hinzu, die auf dieselben Filter reagiert.
3. Erlaube die **Auswahl mehrerer Länder** im Zeitverlauf.
4. Zeichne im Zeitverlauf eine **vertikale Linie für das aktuell gewählte Jahr** ein.
5. Ergänze einen **Download-Button** für die aktuell gefilterten Daten.

## Typische Stolpersteine

- Eine Komponenten-ID darf nur einmal vorkommen.
- Jeder deklarierte `Output` muss von der Callback-Funktion zurückgegeben werden – in derselben Reihenfolge.
- `Dropdown(multi=True)` liefert eine Liste, ein einfaches Dropdown normalerweise einen Einzelwert.
- Leere Filterergebnisse brauchen einen verständlichen Zustand; die App zeigt deshalb eine erklärende leere Figure.
- `debug=True` ist für die Entwicklung praktisch, aber nicht die empfohlene Produktionseinstellung.

