import esankhyiki
import inspect

try:
    print("--- esankhyiki source ---")
    print(inspect.getsource(esankhyiki))
except Exception as e:
    print("Error:", e)
    # Let's inspect the module file path
    import os
    print("File path:", esankhyiki.__file__)
    # Let's list files in the package directory
    pkg_dir = os.path.dirname(esankhyiki.__file__)
    print("Package directory:", pkg_dir)
    print("Package files:", os.listdir(pkg_dir))
    
    # Read the main code file if it's separate
    main_file = os.path.join(pkg_dir, "esankhyiki.py")
    if os.path.exists(main_file):
        print("\n--- esankhyiki.py contents ---")
        with open(main_file, "r", encoding="utf-8") as f:
            print(f.read()[:5000])
