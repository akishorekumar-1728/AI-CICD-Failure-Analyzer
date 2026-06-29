def analyze_error(error):

    if "ModuleNotFoundError" in error:
        return {
            "cause": "A required Python package is missing.",
            "solution": "Install the missing package using pip and add it to requirements.txt."
        }

    elif "SyntaxError" in error:
        return {
            "cause": "Python syntax is incorrect.",
            "solution": "Check the line mentioned in the error and fix the syntax."
        }

    else:
        return {
            "cause": "Unknown error.",
            "solution": "Check GitHub Actions logs."
        }