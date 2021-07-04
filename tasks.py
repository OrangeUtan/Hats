from pathlib import Path

from invoke import task

MEDIA_DIR = Path("./media")


@task
def optimize_media(c):
    showcase_gifs = filter(lambda p: p.name.startswith("showcase"), MEDIA_DIR.iterdir())
    for path in showcase_gifs:
        print(f"Optimizing {path}")
        c.run(f"gifsicle -i {path} -O3 --resize 162x288 --lossy=50 -o {path}")
