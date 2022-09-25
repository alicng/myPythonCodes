from pathlib import pathlib

root_dir = Path('files')
file_paths = root_dir.iterdir()
print(Path.cwd())
for path in file_paths:
    new_filename = "new-" + path.stem + path.suffix
    new_filepath = path.with_name(new_filename)
    print(new_filename)
    path.rename(new_filepath)
    
    
    