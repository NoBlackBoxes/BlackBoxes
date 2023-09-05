# Python : Virtual Environments

Virtual environments are self-contained installations of Python. All of the packages you install and changes you make only affect this *local* environment.

---
## Create a virtual environnmet

- Make a sub-folder in the repository root called "_tmp"
  - *Note*: Anything in the "_tmp" folder is ignored by Git and not synced to the main repository
- Create a Python virtual environment (called "NBB") for working on NoBlackBoxes projects and courses

```bash
mkdir _tmp
cd _tmp
python -m venv NBB
```

- Activate the virtual environment
  - *Note*: You will have to do this each time you want to use your custom Python installation. However, you can get VSCode to automatically activate it for you each time you try to run python.

```bash
# From repo root
source _tmp/NBB/bin/activate
```

## Install useful packages

```bash
pip install numpy matplotlib pyaudio wave
```

## Add local (NBB) libray paths
You can include custom Python libraries by adding a ".pth" file to the *site-packages* folder with the absolute path to your library.

```bash
# From repo root, insert the path (first bit of text) into (>) a *.pth file
echo "/home/${USER}/NoBlackBoxes/LastBlackBox/boxes/audio/python/libs" > _tmp/NBB/lib/python3.11/site-packages/NBB_sound.pth
```

---
