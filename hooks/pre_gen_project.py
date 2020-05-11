import re
import sys

GITLAB_UNAME_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

# module_name = '{{ cookiecutter.module_name }}'
gitlab_username = "{{ cookiecutter.gitlab_username }}"

if not re.match(GITLAB_UNAME_REGEX, gitlab_username):
    print("ERROR: %s is not a valid Python gitlab username!" % gitlab_username)

    # exits with status 1 to indicate failure
    sys.exit(1)
