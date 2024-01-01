import json
import re
from pathlib import Path
def extract_and_save_code_updated(directory_name, output_directory):
    # Define the storage directory path
    storage_dir = Path(f"./Response_from_ChatGPT/{directory_name}")
    output_dir = Path(f"./Code_/{output_directory}")
    output_dir.mkdir(parents=True, exist_ok=True)  # Ensure the output directory exists

    # Regular expression pattern to match between ```
    pattern = r"```[^`]{0,}```"

    # Iterate over the JSON files in the directory
    for json_path in storage_dir.glob("*.json"):
        with open(json_path, "r", encoding="utf8") as jsonFile:
            dic_ = json.load(jsonFile)

            # Extract the needed content from the dictionary
            if "choices" in dic_ and dic_["choices"]:
                content = dic_["choices"][0]["message"]["content"]

                # Use regular expression to find all the code blocks
                code_blocks = re.findall(pattern, content, re.DOTALL)

                # Process and save each code block as a separate file
                for i, code_block in enumerate(code_blocks):
                    # Remove '''python and ''' from the code block
                    code = code_block.replace("```python", " ").replace("```", " ").strip()
                    print(code)
                    # Save the code to a file
                    with open(output_dir / f"{json_path.stem}_code_{i}.py", "w", encoding="utf8") as code_file:
                        code_file.write(code)

# Example usage of the function
directory_name_example = "1st"  # Replace with the actual directory name
output_directory_example = "ch"
extract_and_save_code_updated(directory_name_example, output_directory_example)

