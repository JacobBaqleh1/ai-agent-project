import os

def get_file_content(working_directory: str, file_path: str) -> str:

    try:
        # 1. Get the absolute path of the working directory
        working_dir_abs = os.path.abspath(working_directory)

        # 2. Construct the full normalized path to the target file
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))

         # 3. Check if file_path falls within working_dir_abs
        valid_file_path = os.path.commonpath([working_dir_abs, file_path]) == working_dir_abs

        if not valid_file_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

         # 5. If it's not a file, return error
        if not os.path.isfile(target_dir):
            return f'Error: "{file_path}" is not a file' 
            
               