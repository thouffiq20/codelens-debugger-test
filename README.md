# CodeLens AI Debugger Test Repository

This repository contains intentional Python bugs for testing traceback parsing,
repository-file mapping, root-cause analysis, and fix suggestions.

## Run the first test

From this repository's root folder, run:

```powershell
python -m buggy_app.main
```

Expected error: `ZeroDivisionError: division by zero`

The traceback should reference `buggy_app/main.py` and `buggy_app/calculator.py`.
Import this repository into CodeLens AI, then paste the complete traceback into
the Debugger.

## Other intentional bugs

- `get_user_email(None)` raises an error because `None` is not handled.
- `find_user(users, user_id)` compares the user's name with the ID by mistake.

These bugs are intentional. Do not use this repository in production.
