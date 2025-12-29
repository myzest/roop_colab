#!/usr/bin/env python3
import os
os.environ.pop("MPLBACKEND", None)
os.environ["MPLBACKEND"] = "Agg"

from roop import core

if __name__ == '__main__':
    core.run()
