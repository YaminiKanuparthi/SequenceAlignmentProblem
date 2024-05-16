if [ "$#" -ne 2 ]; then
    echo "Usage: $0 input_file output_file"
    exit 1
fi
python efficient_3.py "$1" "$2"
