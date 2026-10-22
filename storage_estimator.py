# Storage Estimator
# Estimates total storage needed for a number of files.

num_files = int(input("Number of files: "))
size_mb = float(input("Average file size (MB): "))

total_mb = num_files * size_mb
print(f"Total storage needed: {total_mb:.2f} MB")