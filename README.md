### Worknest

A coworking space booking system

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch version-16
bench install-app worknest
```
### Child Table Internals

1. **Database table name:** `tabBooking Add-on Entry`.  
   Frappe stores each DocType's records in its own database table.

2. **Automatically set columns:** `parent`, `parenttype`, `parentfield`, and `idx`.  
   `parent` identifies the parent document, `parenttype` identifies its DocType, `parentfield` identifies the child-table field, and `idx` records the row's position. `parenttype` is needed because different DocTypes can have parent documents with the same name.

3. **Deleting a row:** After saving, the deleted child row is removed from the database, and the remaining rows' `idx` values are renumbered sequentially. The surviving rows retain their `name` values.  
   **Why:** `name` identifies a row, while `idx` represents its position, so `idx` should not be used to remember a specific row between saves.

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/worknest
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade
### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


### License

mit
