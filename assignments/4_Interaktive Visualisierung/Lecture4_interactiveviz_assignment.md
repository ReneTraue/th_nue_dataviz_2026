# Übung zur Vorlesung 4: Interaktive Datenvisualisierung

## Ziel und Umfang

In dieser Übung vergleichst du statische Visualisierungen mit **plotnine** und interaktive Visualisierungen mit **plotly**. 

Wichtig: Du setzt Interaktionen nicht als Selbstzweck ein, sondern prüfst, welche konkrete Analyseaufgabe sie unterstützt.

Im Mittelpunkt steht Shneidermans Prinzip:

> *Overview first, zoom and filter, then details-on-demand.*

Für den Pflichtteil solltest du etwa **60-70 Minuten** einplanen. Wahl- und Bonusaufgaben sind zur Vertiefung gedacht und müssen nicht im selben Termin bearbeitet werden.

## Materialien

- [Übungsnotebook](<Lecture4_interactiveviz_assignment.ipynb>)
- [Plotly-Dokumentation](https://plotly.com/python/)
- [plotnine-Dokumentation](https://plotnine.org/)
- [Gapminder](https://www.gapminder.org/data/)

## Vorbereitung

Öffne das Notebook in VS Code oder Google Colab. Installiere bei Bedarf die verwendeten Pakete:

```python
%pip install plotly pandas plotnine statsmodels 
```

Führe anschließend die Zellen der Reihe nach aus. Das Notebook verwendet den in plotly enthaltenen Gapminder-Datensatz; ein zusätzliches `gapminder`-Paket ist dafür nicht erforderlich.

## Datensatz

Der historische Datensatz umfasst 142 Länder und die Jahre 1952–2007 in Fünfjahresschritten. Er enthält unter anderem:

- `country`: Land
- `continent`: Kontinent
- `year`: Beobachtungsjahr
- `lifeExp`: Lebenserwartung bei Geburt in Jahren
- `pop`: Bevölkerung
- `gdpPercap`: inflationsbereinigtes BIP pro Kopf in US-Dollar

Der Datensatz bildet keine aktuelle Weltstatistik ab. Bei zeitlichen Filtern ist zu beachten, dass zwischen zwei Beobachtungen jeweils fünf Jahre liegen. 

Weitere Infos und mehr Daten aus dem Gapminder Projekt findest Du unter https://www.gapminder.org/data/

## Aufbau der Übung

### Pflichtteil

1. Verteilung der Lebenserwartung als statisches und interaktives Histogramm
2. BIP, Lebenserwartung und Bevölkerung in einem Bubble Chart
3. Kontinentfilter mit einem Plotly-Dropdown
4. Zwei koordinierte Ansichten mit gemeinsamem Filter

### Wahlaufgaben

5. Zeitreihe mit Range Slider und Range Selector
6. Bevölkerungsanteile als Treemap, Donut- und Kreis-Diagramm

### Bonus

7. Vergleich ausgewählter Länder mit wechselbarer Kennzahl
8. Annotation des Bevölkerungsvergleichs zwischen Nigeria und Deutschland
9. Bevölkerungsanteile in Europa

## Qualitätskriterien

Prüfe für jede Visualisierung:

- Ist die Standardansicht als Überblick verständlich?
- Sind Achsen, Einheiten und Datenstand eindeutig beschriftet?
- Ist der aktive Filterzustand erkennbar und zurücksetzbar?
- Liefert Hover zusätzliche, nicht nur wiederholte Information?
- Bleibt die zentrale Aussage auch ohne Interaktion erkennbar?
- Unterstützt die Interaktion eine konkrete Frage oder erzeugt sie nur zusätzliche Bedienung?

Bearbeite den Pflichtteil und beantworte die zugehörigen Reflexionsfragen direkt im Notebook. Dokumentiere bei unvollständigen Lösungen kurz, was bereits funktioniert und an welcher Stelle du noch Unterstützung benötigst.

Eine Musterlösung wird nach der Veranstaltung über das Kurs-Repository bereitgestellt.
