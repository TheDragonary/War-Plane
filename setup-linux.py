from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'include_files': ['backgrounds/', 'fonts/', 'sfx/', 'sprites/'], 'excludes': []}

executables = [
    Executable('main.py', target_name = 'War Plane')
]

setup(name='War Plane',
      version = '1.0',
      description = '',
      options = {'bdist_appimage': build_options},
      executables = executables)
