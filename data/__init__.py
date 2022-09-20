from toml import load


with open("config.toml") as f:
    CONFIG = load(f)