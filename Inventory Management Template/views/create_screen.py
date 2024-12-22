import os
import sys

def create_kivy_screen(project_name):
    # Define folder structure
    folders = [project_name]
    __init__ = f"""from .{project_name} import {project_name.capitalize()}
"""
    main_py_content = f"""from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('views/{project_name}/{project_name}.kv')

class {project_name.capitalize()}(Screen):
    def on_enter(self, *args):
        return super().on_enter(*args)
"""
    kv_content = f"""<{project_name.capitalize()}>:
    BoxLayout:
        orientation: "vertical"
        spacing: "10dp"
"""

    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    # Create __init__ Python file
    with open(os.path.join(project_name, "__init__.py"), "w") as init_file:
        init_file.write(__init__)

    # Create main Python file
    with open(os.path.join(project_name, f"{project_name}.py"), "w") as main_file:
        main_file.write(main_py_content)

    # Create .kv file
    with open(os.path.join(project_name, f"{project_name}.kv"), "w") as kv_file:
        kv_file.write(kv_content)

    print(f"Screen '{project_name}' created successfully!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_screen.py <project_name>")
    else:
        create_kivy_screen(sys.argv[1])
