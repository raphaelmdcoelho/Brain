
### Concepts

In Bash and other shells like Zsh, a Here document (Heredoc) is a type of redirection that allows you to pass multiple lines of input to a command.

```sh
[COMMAND] <<[-] 'DELIMITER'
  HERE-DOCUMENT
DELIMITER
```

The first line starts with an optional command followed by the special redirection operator `<<` and the delimiting identifier.

You can use any string as a delimiting identifier, the most commonly used are EOF or END.

If the delimiting identifier is unquoted, the shell will substitute all variables, commands and special characters before passing the here-document lines to the command.

Appending a minus sign to the redirection operator `<<-`, will cause all leading tab characters to be ignored. This allows you to use indentation when writing here-documents in shell scripts. Leading whitespace characters are not allowed, only tab.

The here-document block can contain strings, variables, commands and any other type of input.

The last line ends with the delimiting identifier. White space in front of the delimiter is not allowed.

### Examples

```sh
cat << EOF
The current working directory is: $PWD
You are logged in as: $(whoami)
EOF

Output
The current working directory is: /home/linuxize
You are logged in as: linuxize
```

If you are using a heredoc inside a statement or loop, use the `<<-` redirection operation that allows you to indent your code.

```sh
if true; then
    cat <<- EOF
    Line with a leading tab.
    EOF
fi
```

```bash
TEST="linhas
line
lines"

grep lines << EOF
$TEST
EOF
```

#technology #computing #shell 