import platform
import sys

# ASCII Art Header
ascii_art = r"""
  _      _       _        
 | |    (_)     (_)       
 | |     _ _ __  _  ___   
 | |    | | '_ \| |/ _ \  
 | |____| | | | | | (_) | 
 |______|_|_| |_|_|\___/  
                           
🔥 Linux Advanced System Info 🔥
"""

print(ascii_art)
print("=" * 40)
print(f"🖥️  OS: {platform.system()} {platform.release()}")
print(f"🛠️  Architecture: {platform.architecture()[0]}")
print(f"⚙️  Processor: {platform.processor()}")
print(f"🐍 Python Version: {sys.version.split()[0]}")
print("=" * 40)
