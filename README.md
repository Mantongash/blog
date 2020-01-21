# The Pitcher

## Author
---
Anthony Ng'ang'a

## Description
___
This is a Flask Blog web app that allows users to create an account and post article. A user can edit and update articles they've created. They can also delete the blogs and comments to their blogs that they deem not appropriate. Other users can then view the articles and comment on them.
___

## Live Link
___
You can find the live link [here](https://pitche.herokuapp.com/)

## BDD
___
![Pitcher Homepage](pitcher/static/images/pitcher.png)

1. Sign Up user on entering correct credentials
  - INPUT: "username"
  - OUTPUT: ""
  - INPUT: "email"
  - OUTPUT: ""
  - INPUT: "password"
  - OUTPUT: ""
  - INPUT: "confirm password"
  - INPUT: ""
2. Error on entering wrong data at Sign Up
  - INPUT: "existing username"
  - OUTPUT: "error notification that there's an existing username"
  - INPUT:  "existing email"
  - OUTPUT: "error notification that there's an existing email"
  - INPUT: "password does not match"
  - OUTPUT: "error notification that password does not match"
3. Adding an article
  - INPUT: "article title"
  - OUTPUT: "article title"
  - INPUT: "article content"
  - OUTPUT: "article content"
4. Adding a comment
  - INPUT: "comment"
  - OUTPUT: "comment"

## Setup Instructions
___
Open the terminal. Move to the directory you want to store the app e.g `cd Desktop`. Then type the following command `git clone https://github.com/Mantongash/pitcher.git`. Once it's done, navigate to the root directory of the app, `cd pitcher`. Then open it with your favorite code editor. Activate the virtual environment `. virtual/bin/activate`. Then install all of the dependencies using `pip install`

## Teachnologies Used
___
```
HTML and CSS (Bootstrap)
Python (Flask)  
```
## Future Plans
- Solve the authentication issue
- Implement a comment feature

### License
MIT Copyright (c) 2019 Anthony Ng'ang'a

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.