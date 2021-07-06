import glob
from pathlib import Path

from invoke import task


@task
def optimize_gif(c, files):
    for path in map(lambda f: Path(f), glob.glob(files)):
        print(f"Optimizing {path}")
        c.run(f"gifsicle -i {path} -O3 --resize 162x288 --lossy=50 -o {path}")
