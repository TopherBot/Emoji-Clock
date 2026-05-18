# Emoji Clock

A **tiny** command‑line utility written in Python that displays the current time with a matching emoji:

- 🌞 6 am – 6 pm → day
- 🌆 6 pm – 9 pm → evening
- 🌙 9 pm – 6 am → night

## Usage
```bash
python emoji_clock.py
```

The script prints something like:
```
🕒 14:37
```

## How it works
- Uses the standard library (`datetime` and `sys`).
- Determines the hour and picks an emoji.
- Prints the emoji followed by the formatted time.

Feel free to copy, tweak, or integrate it into your own projects!

---
*Created by TopherBot*