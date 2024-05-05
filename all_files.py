import os
import main
folder_path = "input_videos"  # Path to the folder containing input videos

# Check if the folder exists
if os.path.exists(folder_path) and os.path.isdir(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Iterate through the files
    for file in files:
        # Check if it's a file (not a directory)
        if os.path.isfile(os.path.join(folder_path, file)):
            # Get the filename without extension
            filename_without_extension = os.path.splitext(file)[0]
            print(filename_without_extension)
            os.environ['video_path'] = 'input_videos/'+str(filename_without_extension)
            os.environ['video_output_path'] = 'output_videos/'+str(filename_without_extension)
            main.main()
else:
    print(f"Folder '{folder_path}' not found or is not a directory.")
