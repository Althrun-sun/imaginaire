
# Compile and install each third-party library individually
echo "Installing third-party libraries..."
for p in correlation channelnorm resample2d bias_act upfirdn2d; do
    echo "Processing third-party library: ${p}..."
    cd imaginaire/third_party/${p} || { echo "Failed to access directory: imaginaire/third_party/${p}"; exit 1; }
    rm -rf build dist *info || { echo "Failed to clean build files for ${p}"; exit 1; }
    echo "Building and installing ${p}..."
    python setup.py install || { echo "Failed to install ${p}"; exit 1; }
    echo "${p} installed successfully."
    cd ${CURRENT} || { echo "Failed to return to ${CURRENT} directory"; exit 1; }
done
echo "All third-party libraries installed successfully."

# Compile each model utility individually
echo "Compiling model utilities..."
for p in gancraft/voxlib; do
    echo "Processing model utility: ${p}..."
    cd imaginaire/model_utils/${p} || { echo "Failed to access directory: imaginaire/model_utils/${p}"; exit 1; }
    echo "Compiling ${p}..."
    make all || { echo "Failed to compile ${p}"; exit 1; }
    echo "${p} compiled successfully."
    cd ${CURRENT} || { echo "Failed to return to ${CURRENT} directory"; exit 1; }
done

echo "Script completed successfully!"
