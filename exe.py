from cx_Freeze import setup, Executable

executables = [
    Executable("math.py")
]

cxfreeze setup.py build
setup(
    name="MathGame",
    version="1.0",
    description="Jeu de math pour nos kids",
    executables=executables
)
