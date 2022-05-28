## Part 1: About the project

Here define:
1. Some colors that you like and that will be relevant for the project. 
    * [Color Palettes, if you need help creating one](http://color.adobe.com/), 
    * [Colorzilla, for choosing colors from your website](http://www.colorzilla.com/)
    [Web Accessibility in Mind - Color Checker](https://webaim.org/resources/contrastchecker/)
2. Some fonts. use [Google Fonts](https://fonts.google.com/).
3. Images you will use. Maybe Lorem Images
    * [Placepuppy](https://place-puppy.com/)
    * [Place Corgi](http://placecorgi.com/)
4. Social media links and the overall links of your project

## Part 2: Working with text 
<sup>All the text but leave the navbar</sup>
1. Think about how you are going to break each one the piece
    * [Lorem Ipsum Generator](https://www.lipsum.com/)
1. Create a good markup. That is convey information in a suitable way. For instance ask to yourself:
    * What is the most important information on this page?
    * What is supporting information or more details
    * Should there be a link? If so, where?
2. Don't forget to validate your HTML here: [HTML Validator](http://validator.w3.org/)

## Part 3: Styling the text
1. always start your styles with the following snippet:

```
/* variables declared here - these are the colors for our pages, as well as the font stacks and sizes. */
:root {
    --black: #171321;
    --dkblue: #0d314b;
    --plum: #4b0d49;
    --hotmag: #ff17e4;
    --magenta: #e310cb;
    --aqua: #86fbfb;
    --white: #f7f8fa;
    --font-size: 1.3rem;
    --mono: "Oxygen mono", monospace;
    --sans: Oxygen, sans-serif;
}

/* border box model: https://css-tricks.com/box-sizing/ */
html {
    box-sizing: border-box;
}
*,
*::before,
*::after {
    box-sizing: inherit;
}
/* generic styles for the page */
body {
    padding: 0;
    margin: 0;
    font-family: var(--sans);
    background-color: var(--black);
    color: var(--white);
    font-size: var(--font-size);
}
h1,
h2,
h3 {
    margin: 0;
}
a {
    color: var(--magenta);
}

a:hover {
    color: var(--hotmag);
    text-decoration: none;
}
```

2. Don't forget to validate your CSS here: [CSS Validator](http://jigsaw.w3.org/css-validator/)

[Choose an open source license](https://choosealicense.com/)

## Part 4: Navbars

1. Markup the HTML
2. Styling the navbar
3. Adding Accessible icons if any
4. Creating a `call for action` button
