import sys
import platform

print("=" * 50)
print("Python Environment Test")
print("=" * 50)
print(f"Python Executable : {sys.executable}")
print(f"Python Version    : {platform.python_version()}")
print(f"Platform          : {platform.platform()}")
print("=" * 50)
