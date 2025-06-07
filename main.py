import plotly.graph_objects as go
import numpy as np

def create_cylinder(x0, y0, z0, radius, height, color):
    theta = np.linspace(0, 2 * np.pi, 30)
    z = np.linspace(0, height, 10)
    theta, z = np.meshgrid(theta, z)
    x = radius * np.cos(theta) + x0
    y = radius * np.sin(theta) + y0
    z = z + z0
    return go.Surface(x=x, y=y, z=z, colorscale=[[0, color], [1, color]], showscale=False)

def create_cone(x0, y0, z0, radius, height, color):
    theta = np.linspace(0, 2 * np.pi, 30)
    r = np.linspace(0, radius, 10)
    theta, r = np.meshgrid(theta, r)
    x = r * np.cos(theta) + x0
    y = r * np.sin(theta) + y0
    z = (1 - r/radius) * height + z0
    return go.Surface(x=x, y=y, z=z, colorscale=[[0, color], [1, color]], showscale=False)

def create_cube(x0, y0, z0, size, color):
    s = size / 2
    X = [x0 - s, x0 + s]
    Y = [y0 - s, y0 + s]
    Z = [z0 - s, z0 + s]
    surfaces = []
    # Enam sisi kubus
    for xi in X:
        surfaces.append(go.Surface(
            x=[[xi, xi], [xi, xi]],
            y=[[Y[0], Y[1]], [Y[0], Y[1]]],
            z=[[Z[0], Z[0]], [Z[1], Z[1]]],
            colorscale=[[0, color], [1, color]], showscale=False
        ))
    for yi in Y:
        surfaces.append(go.Surface(
            x=[[X[0], X[1]], [X[0], X[1]]],
            y=[[yi, yi], [yi, yi]],
            z=[[Z[0], Z[0]], [Z[1], Z[1]]],
            colorscale=[[0, color], [1, color]], showscale=False
        ))
    for zi in Z:
        surfaces.append(go.Surface(
            x=[[X[0], X[1]], [X[0], X[1]]],
            y=[[Y[0], Y[0]], [Y[1], Y[1]]],
            z=[[zi, zi], [zi, zi]],
            colorscale=[[0, color], [1, color]], showscale=False
        ))
    return surfaces

# 🔧 Membuat roket
fig = go.Figure()

# Badan roket (silinder)
fig.add_trace(create_cylinder(0, 0, 0, radius=1, height=4, color='red'))

# Kepala roket (kerucut)
fig.add_trace(create_cone(0, 0, 4, radius=1, height=2, color='orange'))

# Sirip (kubus kecil di kiri, kanan, belakang)
for dx in [-1.2, 1.2]:
    fins = create_cube(dx, 0, 0.5, size=0.6, color='blue')
    for fin in fins:
        fig.add_trace(fin)

back_fins = create_cube(0, -1.2, 0.5, size=0.6, color='blue')
for fin in back_fins:
    fig.add_trace(fin)

# 🔍 Layout
fig.update_layout(
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        aspectratio=dict(x=1, y=1, z=2),
    ),
    margin=dict(l=0, r=0, b=0, t=0)
)

fig.show(renderer="browser")

