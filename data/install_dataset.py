import kagglehub

# Download latest version
path = kagglehub.dataset_download("abuawaish/netflix-dataset")

print("Path to dataset files:", path)