#!/bin/bash

echo "=== FUNNEL ALGORITHM TEST SCRIPT ==="
echo

# Check if files exist
echo "1. Checking required files..."
files=("output.cpp" "enable_debug.h" "Makefile" "algorithm/funnel.h" "algorithm/funnel.cpp")
for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "✓ $file exists"
    else
        echo "✗ $file missing"
    fi
done
echo

# Try simple compilation
echo "2. Testing simple compilation..."
if g++ -std=c++17 -I. -I./algorithm -DFUNNEL_DEBUG -DFUNNEL_DEBUG_FIND_PATH \
    -c output.cpp -o output_test.o 2>/dev/null; then
    echo "✓ output.cpp compiles successfully"
    rm -f output_test.o
else
    echo "✗ output.cpp compilation failed"
    echo "Error details:"
    g++ -std=c++17 -I. -I./algorithm -DFUNNEL_DEBUG -DFUNNEL_DEBUG_FIND_PATH \
        -c output.cpp -o output_test.o 2>&1 | head -5
fi
echo

# Try makefile
echo "3. Testing makefile..."
if make clean >/dev/null 2>&1; then
    echo "✓ Makefile clean works"
else
    echo "✗ Makefile clean failed"
fi

# Check directory structure
echo "4. Checking directory structure..."
echo "Current directory: $(pwd)"
echo "Contents:"
ls -la | grep -E "(algorithm|geometry|algebra|utils|output|enable|Make)"
echo

# Check algorithm directory
echo "5. Checking algorithm directory..."
if [ -d "algorithm" ]; then
    echo "✓ algorithm/ directory exists"
    echo "Contents:"
    ls -la algorithm/
else
    echo "✗ algorithm/ directory missing"
fi
echo

# Final recommendation
echo "6. Recommendations:"
echo "   - If all files exist, try: make run-simple"
echo "   - If compilation fails, check missing dependencies"
echo "   - If algorithm/ missing, copy from correct location"
echo "   - Check README_funnel.md for detailed instructions"
echo

echo "=== END OF TEST ===" 