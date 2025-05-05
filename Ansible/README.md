### What is the difference between the `shell` and `command` modules in Ansible?

#### Answer:
The `shell` and `command` modules in Ansible are used to execute commands on remote hosts, but they have key differences:

- **`command` module**:
    - Executes commands directly without invoking a shell.
    - Does not support shell-specific features like pipes (`|`), redirection (`>`), or environment variable expansion (`$VAR`).
    - Safer to use as it avoids shell injection vulnerabilities.

- **`shell` module**:
    - Executes commands through a shell (e.g., `/bin/sh`).
    - Supports shell-specific features like pipes, redirection, and variable expansion.
    - More flexible but can be less secure due to potential shell injection risks.

**Recommendation**: Use the `command` module when shell features are not required for better security. Use the `shell` module only when shell-specific functionality is necessary.