#!/usr/bin/env python3
"""
Song → Playlist Generator (offline)
Usage:
  python main.py --input "Bohemian Rhapsody"
"""
import argparse, requests, os, sys

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434/api/generate")
MODEL = "llama3.2:4b"
TIMEOUT = 120

def run_llama(prompt):
    r = requests.post(OLLAMA_URL, json={"model": MODEL, "prompt": prompt, "stream": False}, timeout=TIMEOUT)
    r.raise_for_status()
    return r.json().get("response","").strip()

def build_prompt(song):
    return (
        "Create a 10-track playlist similar in vibe to the seed song. Return as numbered list 'N. Artist – Title'.\n"
        f"Seed song: {song}"
    )

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", "-i", required=True, help="Seed song title (optionally artist)")
    args = p.parse_args()
    print(run_llama(build_prompt(args.input)))

if __name__ == "__main__":
    main()
