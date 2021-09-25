# Student Management Software

This is a command-line based Python program for managing Student information using MySQL Database.

## Getting Started

### Prerequisites

1. Python: `v3.x.x`
2. Pip: `v21.x.x`
3. MySQL: `v8.x.x`
4. A clone of this Student Management Software repository on your local machine

_Please install the same versions mentioned above as later/earlier versions might have breaking changes and hence the program might not run as expected._

### Initialization

1. Create a `config.py` file. This file is not provided in this repository for security reasons.
2. Copy and paste the following code in the `config.py` file. Replace the values with your actual database connection credentials.

```python
DB_CONFIG = {
  'host': 'localhost',
  'username': YOUR_USERNAME,
  'password': YOUR_PASSWORD,
  'database': 'school'
}
```

### Running locally

1. Run `initialization.sql` using the terminal or any MySQL Shell app. This is for creating the database and tables necessary to run the app.
2. Run `main.py`. You can either use the terminal or Python IDE Shell.

## FAQs

### What is the purpose of this project?

This program is solely for CBSE evaluation. This project serves no real life purpose and is for educational and evaluation purposes only.

### Can I use this project for my personal purposes?

Yes. However, you are **required** to attribute me, [Syed Basim](https://www.syedbasim.com). This Project is [MIT Licensed](https://github.com/thesyedbasim/student-management/blob/master/LICENSE).

### Is this project being maintained?

No. This project was inteded to be solely for CBSE evaluation. This project, after submission is no longer maintained.

### Are you accepting Pull Requests & Issues?

You are free to open a Pull Request or an Issue. But since this project is not for real life use and not maintained, PRs and Issues won't be accepted and the code will not be merged.

But any PRs which are crucial for the app to run or any issues with which the app is not even performing basic required functions, PRs and Issues are welcome and will be merged.

### Is this a fully functional app?

No. This app can perform only basic CRUD operations for the database.

This app is designed specifically to perform the required operations and not real life use cases. This app is not designed to be scalable.

This app has known issues. You can take a look at all the issues [here](https://github.com/thesyedbasim/student-management/issues). However this app has no intention to prevent these issues and add more features.

### Can I know the technical details of this app?

Yes. You can take a look at the [project synopsis](https://github.com/thesyedbasim/student-management/blob/master/SYNOPSIS.md) for technical details.
