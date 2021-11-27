import cx_Freeze
executables = [cx_Freeze.Executable(
    script="jogo.py", icon="assets/dinoIcon.ico")]

cx_Freeze.setup(
    name="Dino Dead",
    options={"build_exe": {"packages": ["pygame"],
                         "include_files":["assets"] 
                         }},
    executables=executables

)