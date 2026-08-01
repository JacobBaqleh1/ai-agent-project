import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        # 1. Get the absolute path of the working directory
        working_dir_abs = os.path.abspath(working_directory)

        # 2. Construct the full normalized path to the target directory
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        # 3. Check if target_dir falls within working_dir_abs
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        # 4. If outside permitted working directory, return error
        if not valid_target_dir:
            return  f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

         # 5. If it's not a directory, return error
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        items = os.listdir(target_dir)
        lines = []

        for item in items:
            item_path = os.path.join(target_dir, item)
            file_size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)

            lines.append(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")

        return "\n".join(lines)            

    except Exception as e:
           # 7. Catch any unexpected standard library errors
           return f'Error: {e}'
