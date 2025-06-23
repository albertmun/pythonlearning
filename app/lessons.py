LESSONS = [
    {
        'id': 1,
        'title': 'Introduction to Python',
        'description': 'Learn the basics of Python, including syntax, variables, and data types.',
        'content': '''
            <h2>Welcome to your first Python lesson!</h2>
            <p>Python is a versatile and easy-to-learn programming language. Let's start with the classic "Hello, World!" program.</p>
            <pre><code>print("Hello, World!")</code></pre>
            <p>This single line of code will print the message "Hello, World!" to the console. It's a great first step in your programming journey.</p>
        ''',
        'expected_output': 'Hello, World!'
    },
    {
        'id': 2,
        'title': 'Functions and Control Flow',
        'description': 'Understand how to use functions and control the flow of your programs with loops and conditionals.',
        'content': '''
            <h2>Defining and Calling Functions</h2>
            <p>Functions are reusable blocks of code. Here's how you define a simple function:</p>
            <pre><code>def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))</code></pre>
            <p>This code defines a function `greet` that takes a name as input and returns a greeting.</p>
        ''',
        'expected_output': 'Hello, Alice!'
    },
    {
        'id': 3,
        'title': 'Data Structures',
        'description': 'Explore Python\'s built-in data structures like lists, dictionaries, and tuples.',
        'content': '''
            <h2>Working with Lists</h2>
            <p>A list is a collection of items that are ordered and mutable. Here's an example:</p>
            <pre><code>fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)</code></pre>
            <p>This will output `['apple', 'banana', 'cherry', 'orange']`.</p>
        ''',
        'expected_output': "['apple', 'banana', 'cherry', 'orange']"
    }
] 