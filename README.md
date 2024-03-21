## Flask Application Design for Beginner Tamil Website

### HTML Files

- **index.html**: The homepage of the website, providing an introduction to the Tamil language and a list of lessons.
- **lessons.html**: A page displaying a list of all the Tamil lessons available on the website, each with a link to its respective page.
- **lesson1.html**, **lesson2.html**, ...: Individual pages for each Tamil lesson, containing the lesson's content, exercises, and a quiz.

### Routes

- **@app.route('/')**: The root route that displays the homepage (index.html).
- **@app.route('/lessons')**: The route that displays the list of all lessons (lessons.html).
- **@app.route('/lesson/<int:lesson_number>')**: The route that displays a specific lesson (lesson1.html, lesson2.html, etc.) based on the lesson number.
- **@app.route('/lesson/<int:lesson_number>/quiz')**: The route that displays a quiz for the specified lesson (lesson1.html/quiz, lesson2.html/quiz, etc.).