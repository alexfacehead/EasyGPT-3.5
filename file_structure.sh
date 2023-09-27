execute_command() {
    local cmd=$1
    if ! eval "$cmd"; then
        echo "Failed to execute command: $cmd"
        exit 1
    else
        echo "Successfully executed command: $cmd"
    fi
}

print_files() {
    local extensions=$@
    if [ "$extensions" = "--all" ]; then
        extensions="txt cpp h html py c css js java rb php go md xml json csv yaml yml sql png jpeg jpg gif svg"
    fi
    for ext in $extensions; do
        find . -type d -name 'myenv' -prune -o -type f -name "*.$ext" ! -name '*pycache*' ! -name '*.gitignore' -print
    done

main() {
    if [ "$1" = "file_structure" ]; then
        shift
        local source_file=$1
        local destination="/usr/local/bin/file_structure"
    
        # Check if source file exists and is readable
        if [ ! -r "$source_file" ]; then
            echo "Source file $source_file does not exist or is not readable. Please provide an absolute path."
            exit 1
        fi

        # Backup the destination file if it exists and is readable
        if [ -r "$destination" ]; then
            execute_command "sudo cp $destination $destination.copy"
        fi

        # Run the required commands
        execute_command "sudo cp $source_file $destination"
        execute_command "sudo chmod +x $destination"
        execute_command "echo 'alias file_structure=\"$destination\"' >> ~/.zshrc"
    
        echo "Please source your .zshrc file or open a new shell to use the file_structure alias."
    elif [ "$1" = "print_files" ]; then
        shift
        print_files "$@"
    else
        echo "Invalid command. Please use 'file_structure' or 'print_files'."
        exit 1
    fi
}

main "$@"