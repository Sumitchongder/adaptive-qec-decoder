from pathlib import Path


def save_figure(fig, name):

    output = Path("plots/publication")

    output.mkdir(parents=True, exist_ok=True)

    fig.savefig(output / f"{name}.png")

    fig.savefig(output / f"{name}.pdf")

    fig.savefig(output / f"{name}.svg")

    print(f"Saved {name}")
