# Python and Git learning exercises

Small Python exercises preserved from Git/GitHub coursework. This repository is
learning history, not a finished application.

## Files

- `firstpython.py` prints `New python file`.
- `abc.py` checks the sample values 12, 8, and 10 against a strict `> 10`
  threshold. Expected lines are `pass`, `fail`, and `fail`.

## Run

Requires Python 3; no third-party packages or external services are needed.

```bash
python firstpython.py
python abc.py
python -m unittest discover -v
```

Smoke tests verify each script's output and successful exit. GitHub Actions runs
them on Linux. Keep this repository unpinned when showcasing completed projects.

## Reuse

No project license is currently specified. Course attribution and repository
history are preserved; do not infer an open-source license from public access.
