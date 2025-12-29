from matplotlib import colors

def banana_colormap():
    return colors.LinearSegmentedColormap.from_list(
        "banana",
        [
            (0.0, "#99ff33"),
            (0.25, "#ffff00"),
            (0.66, "#ffcc00"),
            (0.75, "#cca300"),
            (0.90, "#6b3e26"),
            (1.0, "#000000"),
        ],
    )
