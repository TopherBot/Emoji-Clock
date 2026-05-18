#!/usr/bin/env python3
"""Emoji Clock – tiny CLI that shows current time with an emoji.

Run:
    python emoji_clock.py
"""
import sys
from datetime import datetime

def get_emoji(hour: int) -> str:
    """Return an emoji based on the hour of the day.
    
    06–18  → 🌞 (day)
    18–21  → 🌆 (evening)
    else   → 🌙 (night)
    """
    if 6 <= hour < 18:
        return "🌞"
    if 18 <= hour < 21:
        return "🌆"
    return "🌙"

def main() -> None:
    now = datetime.now()
    emoji = get_emoji(now.hour)
    time_str = now.strftime("%H:%M")
    print(f"{emoji} {time_str}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
