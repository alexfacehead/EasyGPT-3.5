print_files() {
    find . -type d \( -name '__pycache__' -o -name '.git' -o -name 'venv' -o -name 'myenv' -o -name 'resources' -o -name 'unit_testing' \) -prune -o -type f -name "*.py" -print | while read -r file; do
        if [[ "$file" != *"/constants.py" ]] && [[ "$file" != *"/constants_experimental.py" ]] && [[ "$file" != *"/__init__.py" ]]; then
            printf '`%s`:\n' "$file"
            echo '```py'
            cat "$file"
            echo '```'
            echo '\n'
        fi
    done
}

main() {
    if [ "$1" = "print_files" ]; then
        shift
        print_files "$@"
    else
        echo "Invalid command. Please use 'print_files'."
        exit 1
    fi
}

main "$@"