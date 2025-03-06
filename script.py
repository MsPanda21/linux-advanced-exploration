import platform

print("🔥 Linux Advanced System Info 🔥")
print(f"OS: {platform.system()} {platform.release()}")
print(f"Architecture: {platform.architecture()[0]}")
print(f"Processor: {platform.processor()}")
