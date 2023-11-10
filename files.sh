print_files() {
    # Collect directories to omit
    local -a omit_dirs
    for dir in "$@"; do
        omit_dirs+=( -o -name "$dir" )
    done

    # Construct the find command
    local find_command=( find . -maxdepth 4 -type d \( -name '__pycache__' -o -name '.git' -o -name 'venv' -o -name '*.py' -o -name 'myenv' -o -name 'resources' -o -name 'unit_testing' "${omit_dirs[@]}" \) -prune -o -type f -print )

    # Execute the find command and process files
    "${find_command[@]}" | while IFS= read -r file; do
        # Determine filetype based on file extension
        filetype=""
        case "$file" in
            *.py)
                filetype="python"
                ;;
            *.ts)
                filetype="typescript"
                ;;
            *.js)
                filetype="javascript"
                ;;
            *.css)
                filetype="css"
                ;;
            *.html)
                filetype="html"
                ;;
            # Add other filetypes here if needed
        esac

        # Skip specific python files, adjust if you have similar rules for other filetypes
        if [[ "$filetype" == "python" ]] && { [[ "$file" == *"/constants.py" ]] || [[ "$file" == *"/constants_experimental.py" ]] || [[ "$file" == *"/__init__.py" ]]; }; then
            continue
        fi

        # Only print if filetype is known
        if [[ -n "$filetype" ]]; then
            printf '`%s`:\n' "$file"
            echo "\`\`\`$filetype"
            cat "$file"
            echo "\`\`\`"
            echo
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