# Project Name: PYTHON ARTICLE

## Overview
This project involves creating three classes: `Author`, `Article`, and `Magazine` to track the relationships between authors, articles, and magazines. An author can have many articles, a magazine can have many articles, and articles belong to both an author and a magazine. The relationship between `Author` and `Magazine` is many-to-many. This README file provides instructions on how to implement these classes and their methods.

## Getting Started
Before you begin, make sure you have all the dependencies required for this project installed. You can use the provided `Pipfile` as a reference to set up your virtual environment and install the required packages. This project is designed for Python 3.10.

```shell
# Install dependencies using Pipenv (assuming you have Pipenv installed)
pipenv install
```

## Class Definitions

### Author
- `Author __init__(name: str)`
  - Initialize an author with a name as a string.
  - The author's name **cannot** be changed after initialization.
- `Author name() -> str`
  - Returns the name of the author.
- `Author articles() -> List[Article]`
  - Returns a list of Article instances written by the author.
- `Author magazines() -> List[Magazine]`
  - Returns a **unique** list of Magazine instances for which the author has contributed.

### Magazine
- `Magazine __init__(name: str, category: str)`
  - Initialize a magazine with a name and a category, both as strings.
  - The name and category of the magazine **can be** changed after initialization.
- `Magazine name() -> str`
  - Returns the name of the magazine.
- `Magazine category() -> str`
  - Returns the category of the magazine.
- `Magazine all() -> List[Magazine]`
  - Returns a list of all Magazine instances.
- `Magazine contributors() -> List[Author]`
  - Returns a list of Author instances who have written for this magazine.
- `Magazine find_by_name(name: str) -> Magazine (class method)`
  - Given a string representing the magazine's name, this method returns the first magazine object that matches.
- `Magazine article_titles() -> List[str] (class method)`
  - Returns a list of strings containing the titles of all articles written for that magazine.
- `Magazine contributing_authors() -> List[Author]`
  - Returns a list of authors who have written more than 2 articles for the magazine.

### Article
- `Article __init__(author: Author, magazine: Magazine, title: str)`
  - Initialize an article with an author as an Author object, a magazine as a Magazine object, and a title as a string.
  - An article **cannot** change its author, magazine, or title after initialization.
- `Article title() -> str`
  - Returns the title of the article.
- `Article author() -> Author`
  - Returns the author of the article.
- `Article magazine() -> Magazine`
  - Returns the magazine of the article.
- `Article all() -> List[Article]`
  - Returns a list of all Article instances.

## Instructions
1. Create a folder for your project and name it appropriately.
2. Inside the project folder, create three Python files: `Author.py`, `Article.py`, and `Magazine.py`. Implement the classes and methods according to the provided specifications.
3. Ensure that you create sample instances and test your code in the Python console to verify that it works as expected.
4. Prioritize writing methods that work over writing more methods that don't work. Test and debug your code as you go along.
5. If you encounter duplicated logic, consider extracting it into shared helper methods.
6. Save and run your code to verify that it works as expected before submitting.

## Deliverables
Your project structure should look like this:

```
project_folder/
│
├── Author.py
├── Article.py
├── Magazine.py
├── Pipfile
│
└── README.md (this file)
```

Ensure that your code adheres to best practices and is well-documented. Include comments where necessary to explain your code's functionality.

## Additional Notes
- Writing error-free code is more important than completing all deliverables. Prioritize functional methods over incomplete ones.
- You are encouraged to draw your domain on paper or a whiteboard before starting coding to visualize the relationships between classes.
- Test your code in the console and ensure that all methods work as expected.
- Feel free to refactor your code for best practices and code readability once your methods are working correctly.