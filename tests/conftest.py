import sys
from pathlib import Path

# Add the project root directory to sys.path so tests can import server, admin, and main
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
