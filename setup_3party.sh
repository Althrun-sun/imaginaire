# # Compile and install the correlation third-party library
# echo "Installing third-party libraries..."

# # Process correlation library
# echo "Processing third-party library: correlation..."

# # Navigate to the correct directory
# cd imaginaire/third_party/correlation || { echo "Failed to access directory: imaginaire/third_party/correlation"; exit 1; }

# # Clean previous build files
# rm -rf build dist *info || { echo "Failed to clean build files for correlation"; exit 1; }

# # Specify the src path to match the updated setup.py structure
# echo "Building and installing correlation..."
# python setup.py install || { echo "Failed to install correlation"; exit 1; }
# echo "correlation installed successfully."

# # Return to the initial directory
# cd "$CURRENT" || { echo "Failed to return to ${CURRENT} directory"; exit 1; }




# Compile and install the channelnorm third-party library
echo "Processing third-party library: channelnorm..."

# Navigate to the correct directory
cd imaginaire/third_party/channelnorm || { echo "Failed to access directory: imaginaire/third_party/channelnorm"; exit 1; }

# Clean previous build files
rm -rf build dist *info || { echo "Failed to clean build files for channelnorm"; exit 1; }

# Specify the src path to match the updated setup.py structure
echo "Building and installing channelnorm..."
python setup.py install || { echo "Failed to install channelnorm"; exit 1; }
echo "channelnorm installed successfully."

# Return to the initial directory
cd "$CURRENT" || { echo "Failed to return to ${CURRENT} directory"; exit 1; }



# # Process resample2d library
# echo "Processing third-party library: resample2d..."
# cd imaginaire/third_party/resample2d || { echo "Failed to access directory: imaginaire/third_party/resample2d"; exit 1; }
# rm -rf build dist *info || { echo "Failed to clean build files for resample2d"; exit 1; }
# echo "Building and installing resample2d..."
# python setup.py install || { echo "Failed to install resample2d"; exit 1; }
# echo "resample2d installed successfully."
# cd ${CURRENT} || { echo "Failed to return to ${CURRENT} directory"; exit 1; }

# # Process bias_act library
# echo "Processing third-party library: bias_act..."
# cd imaginaire/third_party/bias_act || { echo "Failed to access directory: imaginaire/third_party/bias_act"; exit 1; }
# rm -rf build dist *info || { echo "Failed to clean build files for bias_act"; exit 1; }
# echo "Building and installing bias_act..."
# python setup.py install || { echo "Failed to install bias_act"; exit 1; }
# echo "bias_act installed successfully."
# cd ${CURRENT} || { echo "Failed to return to ${CURRENT} directory"; exit 1; }

# # Process upfirdn2d library
# echo "Processing third-party library: upfirdn2d..."
# cd imaginaire/third_party/upfirdn2d || { echo "Failed to access directory: imaginaire/third_party/upfirdn2d"; exit 1; }
# rm -rf build dist *info || { echo "Failed to clean build files for upfirdn2d"; exit 1; }
# echo "Building and installing upfirdn2d..."
# python setup.py install || { echo "Failed to install upfirdn2d"; exit 1; }
# echo "upfirdn2d installed successfully."
# cd ${CURRENT} || { echo "Failed to return to ${CURRENT} directory"; exit 1; }

echo "All third-party libraries installed successfully."
