import re

def parse_rsp(rsp, fmt="json"):
    pattern = r"```{}(.*?)```".format(fmt)  # ? means non-greedy match
    matches = re.findall(pattern, rsp, re.DOTALL)
    cmd_text = matches[-1] if matches else ""
    return cmd_text

def unify_id(id):
    """Unify id format, e.g., RFC2328.1.1.1 and 1.1.1 and 1.1.1."""
    if id.startswith("RFC"):
        id = '.'.join(id.split('.')[1:])
    if id.endswith("."):
        id = id[:-1]
    return id
