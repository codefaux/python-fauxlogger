# fauxlogger

A dead simple, lightweight, zero-dependency Python logging helper with readable, colorized output including short trace, timestamps, and thread safety for multiline output without interruption.

## Install

```bash
pip install -e .
```

## Usage

```python
import fauxlogger as _log
_log.msg(f"{_log._BLUE}Test me{_log.RESET}")
```

## Demo

(Unrelated output, as demo)
<img width="1449" height="544" alt="image" src="https://github.com/user-attachments/assets/fb9409b0-dd55-4919-b243-bd6349d87c08" />
