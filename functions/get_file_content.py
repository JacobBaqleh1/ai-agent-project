import os

def get_file_content(working_directory: str, file_path: str) -> str:

    try:
        # 1. Get the absolute path of the working directory
        working_dir_abs = os.path.abspath(working_directory)

        # 2. Construct the full normalized path to the target file
        target_path = os.path.abspath(os.path.join(working_dir_abs, file_path))

         # 3. Check if file_path falls within working_dir_abs
        valid_file_path = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs

        if not valid_file_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

         # 5. If it's not a file, return error
        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"' 

        MAX_CHARS = 10000

        with open(target_path, "r", encoding="utf-8") as f: 
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'    
        return content 

    except Exception as e:
        return f"Error: {str(e)}"          