import importlib

for name in ["numpy", "matplotlib", "cv2", "sklearn",
             "serial", "flask", "pybullet", "pytest"]:
    try:
        m = importlib.import_module(name)
        ver = getattr(m, "__version__", "ok")
        print(f"{name:10s} {ver}")
    except ImportError:
        print(f"{name:10s} MISSING")
