# Lecture 2: Statische Visualisierung

Diese Seite fasst die Lab Session zusammen und dient als Referenz beim Bearbeiten der Aufgaben.

## Materialien

- [Jupyter-Notebook: Lecture2_assignment.ipynb](<assignments/3_Statische Visualisierung/Lecture2_assignment.ipynb>)
- [Python-Tutorial: Einrichtung und Grundlagen](<assignments/2_Visuelle_Wahrnehmung/tutorial_python.md>)

## Vorbereitung

1. Öffnen Sie das Notebook in Jupyter, VS Code oder Google Colab.
2. Falls die benötigten Pakete noch nicht installiert sind, führen Sie in einer Notebook-Zelle aus:

   ```python
   %pip install gapminder pandas plotnine
   ```

3. Führen Sie die Setup- und Import-Zellen der Reihe nach aus. Falls Sie den Kernel oder die Laufzeit neu starten, führen Sie die Zellen erneut von oben aus.
4. Tragen Sie Ihre Namen in die dafür vorgesehene Zelle ein und bearbeiten Sie die Aufgaben direkt im Notebook.

Hinweise zum Einrichten von Python, Jupyter und den Arbeitsumgebungen finden Sie im [Python-Tutorial](<assignments/2_Visuelle_Wahrnehmung/tutorial_python.md>).

## Der Gapminder-Datensatz

Das Notebook verwendet den historischen Gapminder-Lehrdatensatz. Er enthält Beobachtungen zu 142 Ländern für zwölf Jahre von 1952 bis 2007, jeweils in Fünfjahresschritten. Zu den verwendeten Merkmalen gehören:

- `country`: Land
- `continent`: Kontinent
- `year`: Beobachtungsjahr
- `lifeExp`: Lebenserwartung
- `pop`: Bevölkerung
- `gdpPercap`: BIP pro Kopf

Der Datensatz eignet sich dazu, Beziehungen und Veränderungen über Länder, Kontinente und Zeit hinweg zu untersuchen. Er ist ein historischer Lehrdatensatz und keine aktuelle oder vollständige Weltstatistik.

Weitere Informationen:

- [Dokumentation des Gapminder-Datensatzes](https://jennybc.github.io/gapminder/reference/gapminder.html)
- [Gapminder-Daten als CSV im Plotly-Datasets-Repository](https://github.com/plotly/datasets/blob/master/gapminderDataFiveYear.csv)

## Aufgabenüberblick

Bearbeiten Sie die Aufgaben im Notebook und halten Sie Ihre Beobachtungen bei den jeweiligen Grafiken fest.

1. **Einkommen und Lebenserwartung:** Untersuchen Sie den Zusammenhang zwischen `gdpPercap` und `lifeExp`. Vergleichen Sie eine lineare mit einer logarithmischen x-Achse und überlegen Sie, wie die Skalenwahl die Interpretation verändert.
2. **Verteilungen nach Kontinent (2007):** Vergleichen Sie die Lebenserwartung der Kontinente mit unterschiedlichen Verteilungsplots. Recherchieren Sie bei Bedarf weitere Plot-Arten, zum Beispiel über [anyplot.ai/plots](https://anyplot.ai/plots).
3. **Veränderung über die Zeit:** Visualisieren Sie die Entwicklung der Lebenserwartung nach Kontinenten. Achten Sie darauf, dass die Länder als getrennte Gruppen dargestellt werden, und nutzen Sie Facets zum Vergleich der Kontinente. Überlegen Sie anschließend, wie ausgewählte Länder hervorgehoben werden könnten.
4. **Wohlstand und Lebenserwartung im Zeitverlauf:** Untersuchen Sie, wie sich der Zusammenhang zwischen Einkommen und Lebenserwartung über die Jahrzehnte verändert. Nutzen Sie Facets, um mehrere Jahre oder Zeitabschnitte vergleichbar darzustellen, und interpretieren Sie mögliche Annäherungen oder Unterschiede zwischen Kontinenten.

### Bonus: Themes

Probieren Sie ein anderes Plot-Theme aus und beurteilen Sie, wie sich die Gestaltung auf Lesbarkeit und Wirkung der Grafik auswirkt. Als Einstieg dient der [plotnine-Guide zu vorgefertigten Themes](https://plotnine.org/guide/themes-premade.html).

## Worauf Sie achten sollten

- Wählen Sie Diagrammtyp und Skala passend zur Fragestellung.
- Beschriften Sie Achsen und Legenden verständlich.
- Nutzen Sie Farbe und Gruppierung bewusst und konsistent.
- Beschreiben Sie, welches Muster die Grafik zeigt und welche Einschränkungen bei der Interpretation gelten.
- Führen Sie die Zellen im Notebook aus und speichern Sie Ihre Arbeit.
