"""
File Handling Master Program
Author: Natnael
Date: 2024
Description: A robust file handling program that reads, modifies, and writes files
with comprehensive error handling and user-friendly interface.
"""

import os

def read_file(filename):
    """
    Read content from a file with error handling
    
    Args:
        filename (str): Name of the file to read
        
    Returns:
        str: Content of the file or None if error occurs
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        print(f"✅ Successfully read '{filename}'")
        return content
    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
        return None
    except PermissionError:
        print(f"❌ Error: Permission denied to read '{filename}'.")
        return None
    except UnicodeDecodeError:
        print(f"❌ Error: Could not decode the file '{filename}'. It might be a binary file.")
        return None
    except Exception as e:
        print(f"❌ Unexpected error reading '{filename}': {e}")
        return None

def write_file(filename, content):
    """
    Write content to a file with error handling
    
    Args:
        filename (str): Name of the file to write to
        content (str): Content to write to the file
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"✅ Successfully wrote to '{filename}'")
        return True
    except PermissionError:
        print(f"❌ Error: Permission denied to write to '{filename}'.")
        return False
    except Exception as e:
        print(f"❌ Unexpected error writing to '{filename}': {e}")
        return False

def modify_content(content):
    """
    Modify the file content (example transformation)
    
    Args:
        content (str): Original content
        
    Returns:
        str: Modified content
    """
    if content is None:
        return None
        
    # Example modifications:
    # 1. Convert to uppercase
    # 2. Add line numbers
    # 3. Add a header and footer
    
    lines = content.split('\n')
    modified_lines = []
    
    # Add header
    modified_lines.append("📄 MODIFIED FILE CONTENT")
    modified_lines.append("=" * 40)
    modified_lines.append("")
    
    # Add content with line numbers
    for i, line in enumerate(lines, 1):
        modified_lines.append(f"{i:3d}. {line.upper()}")
    
    # Add footer
    modified_lines.append("")
    modified_lines.append("=" * 40)
    modified_lines.append("🎉 End of modified content")
    
    return '\n'.join(modified_lines)

def get_valid_filename(prompt):
    """
    Get a valid filename from user with validation
    
    Args:
        prompt (str): Prompt to display to user
        
    Returns:
        str: Valid filename or None if user wants to quit
    """
    while True:
        filename = input(prompt).strip()
        
        if filename.lower() in ['quit', 'exit', 'q']:
            return None
            
        if not filename:
            print("⚠️ Please enter a filename.")
            continue
            
        # Check for invalid characters (basic validation)
        invalid_chars = '<>:"/\\|?*'
        if any(char in filename for char in invalid_chars):
            print(f"❌ Filename contains invalid characters. Avoid: {invalid_chars}")
            continue
            
        return filename

def main():
    """
    Main function to run the file handling program
    """
    print("🎯 File Handling Master Program")
    print("=" * 40)
    print("This program reads a file, modifies its content,")
    print("and writes the modified version to a new file.")
    print("Type 'quit' at any time to exit.")
    print("=" * 40)
    
    # Get input filename
    input_file = get_valid_filename("\n📖 Enter the input filename: ")
    if input_file is None:
        print("👋 Exiting program.")
        return
    
    # Read the file
    original_content = read_file(input_file)
    if original_content is None:
        return
    
    # Display original content preview
    print(f"\n📋 Original content preview (first 200 chars):")
    print("-" * 50)
    preview = original_content[:200] + ("..." if len(original_content) > 200 else "")
    print(preview)
    print("-" * 50)
    
    # Modify content
    modified_content = modify_content(original_content)
    
    # Get output filename
    output_file = get_valid_filename("\n💾 Enter the output filename: ")
    if output_file is None:
        print("👋 Exiting program.")
        return
    
    # Check if output file already exists
    if os.path.exists(output_file):
        overwrite = input(f"⚠️  '{output_file}' already exists. Overwrite? (y/n): ").lower()
        if overwrite != 'y':
            print("Operation cancelled.")
            return
    
    # Write modified content
    if write_file(output_file, modified_content):
        print(f"\n🎉 Success! Modified content written to '{output_file}'")
        
        # Show final file info
        if os.path.exists(output_file):
            file_size = os.path.getsize(output_file)
            print(f"📊 Output file size: {file_size} bytes")
    
    print("\n" + "=" * 40)
    print("Thank you for using the File Handling Master Program!")
    print("=" * 40)

def run_example():
    """
    Run an example demonstration with test files
    """
    print("🧪 Running example demonstration...")
    
    # Create a test file
    test_content = """Hello, World!
This is a test file.
Python file handling is powerful!
We can read, modify, and write files.
Exception handling makes our code robust."""
    
    write_file("example_input.txt", test_content)
    
    # Read and modify
    content = read_file("example_input.txt")
    if content:
        modified = modify_content(content)
        write_file("example_output.txt", modified)
        print("✅ Example completed! Check 'example_output.txt'")

if __name__ == "__main__":
    # Uncomment the next line to run the example demonstration
    # run_example()
    
    # Run the main interactive program
    main()
