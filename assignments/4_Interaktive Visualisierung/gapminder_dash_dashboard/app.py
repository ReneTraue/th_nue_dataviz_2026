""" Plotly-Dash-Dashboard auf Basis des Gapminder-Datensatzes."""

from __future__ import annotations

from dash import Dash, Input, Output, callback, dcc, html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# 1. Daten laden und Konstanten definieren
DF = px.data.gapminder()
# Native Python-Typen vermeiden JSON-Probleme mit NumPy-Skalaren im Dash-Layout.
YEARS = sorted(int(year) for year in DF["year"].unique())
CONTINENTS = sorted(str(continent) for continent in DF["continent"].unique())

COLORS = {
    "Africa": "#E76F51",
    "Americas": "#2A9D8F",
    "Asia": "#E9C46A",
    "Europe": "#457B9D",
    "Oceania": "#8E6C88",
}

METRICS = {
    "lifeExp": ("Lebenserwartung", "Jahre"),
    "gdpPercap": ("BIP pro Kopf", "US-Dollar"),
    "pop": ("Bevölkerung", "Menschen"),
}


def filter_data(year: int, continents: list[str] | None) -> pd.DataFrame:
    """Zentrale Filterfunktion: eine Datenbasis für alle Kennzahlen und Charts."""
    selected = CONTINENTS if continents is None else continents
    return DF[(DF["year"] == year) & (DF["continent"].isin(selected))].copy()


def empty_figure(message: str) -> go.Figure:
    """Lesbarer Leerzustand, falls ein Filter keine Zeilen zurückgibt."""
    figure = go.Figure()
    figure.add_annotation(
        text=message,
        x=0.5,
        y=0.5,
        xref="paper",
        yref="paper",
        showarrow=False,
        font={"size": 18, "color": "#52606d"},
    )
    figure.update_layout(template="plotly_white", xaxis={"visible": False}, yaxis={"visible": False})
    return figure


def format_compact(value: float) -> str:
    """Große Zahlen platzsparend und deutsch lesbar ausgeben."""
    if value >= 1_000_000_000:
        return f"{value / 1_000_000_000:.2f} Mrd."
    if value >= 1_000_000:
        return f"{value / 1_000_000:.1f} Mio."
    return f"{value:,.0f}".replace(",", ".")


# 2. App und statisches Layout definieren
app = Dash(__name__)
app.title = "Gapminder Explorer"
server = app.server

app.layout = html.Div(
    className="app-shell",
    children=[
        html.Header(
            className="hero",
            children=[
                html.Div("INTERAKTIVE DATENVISUALISIERUNG", className="eyebrow"),
                html.H1("Gapminder Explorer"),
                html.P(
                    "Wie hängen Wohlstand, Lebenserwartung und Bevölkerung zusammen? "
                    "Filtere die Welt, vergleiche Kontinente und folge einzelnen Ländern durch die Zeit."
                ),
            ],
        ),
        html.Main(
            children=[
                html.Section(
                    className="control-panel",
                    children=[
                        html.Div(
                            className="control control-year",
                            children=[
                                html.Label("Jahr", htmlFor="year-slider"),
                                dcc.Slider(
                                    id="year-slider",
                                    min=min(YEARS),
                                    max=max(YEARS),
                                    step=None,
                                    value=max(YEARS),
                                    marks={year: str(year) for year in YEARS},
                                    tooltip={"placement": "bottom", "always_visible": False},
                                ),
                            ],
                        ),
                        html.Div(
                            className="control",
                            children=[
                                html.Label("Kontinente", htmlFor="continent-filter"),
                                dcc.Dropdown(
                                    id="continent-filter",
                                    options=[{"label": item, "value": item} for item in CONTINENTS],
                                    value=CONTINENTS,
                                    multi=True,
                                    clearable=True,
                                    placeholder="Kontinent wählen …",
                                ),
                            ],
                        ),
                        html.Div(
                            className="control",
                            children=[
                                html.Label("Kennzahl im Zeitverlauf", htmlFor="metric-select"),
                                dcc.RadioItems(
                                    id="metric-select",
                                    options=[
                                        {"label": label, "value": key}
                                        for key, (label, _unit) in METRICS.items()
                                    ],
                                    value="lifeExp",
                                    className="radio-group",
                                ),
                            ],
                        ),
                    ],
                ),
                html.Div(id="kpi-row", className="kpi-grid"),
                html.Section(
                    className="chart-card chart-card-wide",
                    children=[
                        html.Div(
                            className="card-heading",
                            children=[
                                html.Div(
                                    [
                                        html.Span("ÜBERBLICK", className="section-tag"),
                                        html.H2("Wohlstand und Lebenserwartung"),
                                    ]
                                ),
                                html.P("Punktgröße = Bevölkerung · Klicke auf ein Land für den Zeitverlauf"),
                            ],
                        ),
                        dcc.Graph(id="bubble-chart", config={"displaylogo": False}),
                    ],
                ),
                html.Div(
                    className="chart-grid",
                    children=[
                        html.Section(
                            className="chart-card",
                            children=[
                                html.Div(
                                    className="card-heading",
                                    children=[
                                        html.Div(
                                            [
                                                html.Span("VERTEILUNG", className="section-tag"),
                                                html.H2("Lebenserwartung"),
                                            ]
                                        ),
                                        html.P("Eine gemeinsame Filterung verbindet die Ansichten"),
                                    ],
                                ),
                                dcc.Graph(id="histogram", config={"displaylogo": False}),
                            ],
                        ),
                        html.Section(
                            className="chart-card",
                            children=[
                                html.Div(
                                    className="card-heading",
                                    children=[
                                        html.Div(
                                            [
                                                html.Span("DETAIL", className="section-tag"),
                                                html.H2(id="detail-title"),
                                            ]
                                        ),
                                        html.P("Auswahl per Klick im Bubble Chart"),
                                    ],
                                ),
                                dcc.Graph(id="country-history", config={"displaylogo": False}),
                            ],
                        ),
                    ],
                ),
                html.Section(
                    className="learning-card",
                    children=[
                        html.Span("Interaktive Datenvisualisierung - Prinzipien", className="section-tag"),
                        html.H2("Overview first, zoom and filter, then details-on-demand"),
                        html.Div(
                            className="learning-grid",
                            children=[
                                html.Div([html.Strong("1 · Overview"), html.P("Bubble Chart und Kennzahlen zeigen das Gesamtbild.")]),
                                html.Div([html.Strong("2 · Zoom & Filter"), html.P("Jahr und Kontinente grenzen die Analyse ein.")]),
                                html.Div([html.Strong("3 · Details"), html.P("Hover und Klick erschließen einzelne Länder.")]),
                            ],
                        ),
                    ],
                ),
            ]
        ),
        html.Footer("Datengrundlage: Gapminder · Demo mit Plotly Dash"),
    ],
)


# 3. Reaktive Logik: Inputs verändern mehrere Outputs
@callback(
    Output("kpi-row", "children"),
    Output("bubble-chart", "figure"),
    Output("histogram", "figure"),
    Input("year-slider", "value"),
    Input("continent-filter", "value"),
)
def update_overview(year: int, continents: list[str] | None):
    """Aktualisiert alle Übersichten aus derselben gefilterten Datenbasis."""
    data = filter_data(year, continents)

    if data.empty:
        kpis = [
            html.Div(
                className="kpi-card kpi-empty",
                children=[html.Span("Keine Daten"), html.Strong("–"), html.Small("Filter anpassen")],
            )
        ]
        return kpis, empty_figure("Keine Länder ausgewählt"), empty_figure("Keine Daten für die Auswahl")

    kpi_values = [
        ("Länder", f"{len(data)}", f"im Jahr {year}"),
        ("Bevölkerung", format_compact(data["pop"].sum()), "in der Auswahl"),
        ("Median Lebenserwartung", f"{data['lifeExp'].median():.1f} Jahre", "robust gegen Ausreißer"),
        ("Median BIP/Kopf", f"{data['gdpPercap'].median():,.0f} $".replace(",", "."), "logarithmische X-Achse"),
    ]
    kpis = [
        html.Div(
            className="kpi-card",
            children=[html.Span(label), html.Strong(value), html.Small(note)],
        )
        for label, value, note in kpi_values
    ]

    bubble = px.scatter(
        data,
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        color_discrete_map=COLORS,
        hover_name="country",
        hover_data={"gdpPercap": ":,.0f", "lifeExp": ":.1f", "pop": ":,.0f", "continent": True},
        custom_data=["country"],
        log_x=True,
        size_max=62,
        labels={
            "gdpPercap": "BIP pro Kopf (US-Dollar, logarithmisch)",
            "lifeExp": "Lebenserwartung (Jahre)",
            "continent": "Kontinent",
        },
    )
    bubble.update_traces(marker={"line": {"width": 1.2, "color": "white"}, "opacity": 0.82})
    bubble.update_layout(
        template="plotly_white",
        margin={"l": 20, "r": 20, "t": 20, "b": 20},
        legend={"orientation": "h", "y": 1.08, "x": 0},
        hovermode="closest",
        transition_duration=250,
    )

    histogram = px.histogram(
        data,
        x="lifeExp",
        color="continent",
        color_discrete_map=COLORS,
        nbins=20,
        barmode="overlay",
        opacity=0.72,
        labels={"lifeExp": "Lebenserwartung (Jahre)", "count": "Anzahl Länder", "continent": "Kontinent"},
    )
    histogram.update_layout(
        template="plotly_white",
        margin={"l": 20, "r": 20, "t": 20, "b": 20},
        showlegend=False,
        bargap=0.08,
    )

    return kpis, bubble, histogram


@callback(
    Output("country-history", "figure"),
    Output("detail-title", "children"),
    Input("bubble-chart", "clickData"),
    Input("metric-select", "value"),
)
def update_country_history(click_data: dict | None, metric: str):
    """Zeigt Details zum angeklickten Land; Deutschland ist der verständliche Startwert."""
    country = "Germany"
    if click_data and click_data.get("points"):
        point = click_data["points"][0]
        custom_data = point.get("customdata")
        if custom_data:
            country = custom_data[0]

    country_data = DF[DF["country"] == country].sort_values("year")
    label, unit = METRICS[metric]

    figure = px.line(
        country_data,
        x="year",
        y=metric,
        markers=True,
        labels={"year": "Jahr", metric: f"{label} ({unit})"},
    )
    figure.update_traces(
        line={"color": "#184E77", "width": 3},
        marker={"size": 7, "color": "#F4A261", "line": {"width": 1, "color": "white"}},
        hovertemplate=f"Jahr: %{{x}}<br>{label}: %{{y:,.2f}}<extra></extra>",
    )
    figure.update_layout(
        template="plotly_white",
        margin={"l": 20, "r": 20, "t": 20, "b": 20},
        hovermode="x unified",
    )
    return figure, f"{country}: {label}"


if __name__ == "__main__":
    app.run(debug=True)