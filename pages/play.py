import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc


column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Choose your character
            """
        ),
        dcc.Dropdown(id = 'character_select',
                     options = None,
                     searchable=True,
                     )
    ]
)

layout = dbc.Row([column1])
