# Refactoring _preloader.scss: ASCII sci-fi terminal boot sequence

**Session ID:** ses_47ab2995dffeAmMJyDAbvy8jCn
**Created:** 1/4/2026, 12:50:00 AM
**Updated:** 1/4/2026, 12:51:51 AM

---

## User

i am not statisfied with current @_preloader.scss file. I want to remove all the animation and make it look more 'sci-fi looking terminal boot sequence' but use typography only and ASCII style only 

---

## Assistant

 To create a sci-fi looking terminal boot sequence with ASCII typography, follow these steps:

1. First, note that CSS preloader animations are visually distinct from ASCII-style terminal sequences. You will want to completely delete the existing code in your @_preloader.scss file.

2. To create an ASCIIGlyphs boot sequence, make use of online tools such as  https://www.geeksforgeeks.org/ascii-art/ or https://patorjk.com/software/taag/. Create separate terminal art images for different stages of the loading process (e.g., loading bars, logos, messages).

3. Save each image as a separate .txt file in your project directory or asset folder (e.g., logo-loading1.txt, bar1.txt, bar2.txt, and so on.). Make sure to keep them organized for easy reference later on.

4. Next, load each ASCII art file successively while changing the visibility of other elements using JavaScript to simulate a loading sequence.

5. To display these ASCII images as terminal-style text in your CSS preloader, use pseudo-elements (::before and ::after) with content properties to insert these image contents into specific elements.

6. Modify the visibility property of each pseudo-element based on JavaScript handling of loading progress for a smooth animation effect.

For example, consider this simplified structure:

HTML
```html
<div id="preloader">
  <div class="preloader-content">
    <div class="loading1" style="visibility:hidden"></div> <!-- Loading content goes here -->
    <div class="loading2" style="visibility:hidden"></div>
    ...
    <div id="message"></div>
  </div>
</div>
```

SCSS:

```scss
#preloader {
  .preloader-content {
    .loading1, .loading2 { /* CSS for each loading state goes here */ }
  }
}

#preloader .loading1::before, #preloader .loading1::after {
  content: url(logo-loading1.txt);
}

#preloader .loading2::before, #preloader .loading2::after {
  content: url(bar1.txt);
}
...
```

7. In your JavaScript file, write a function that updates the visibility of pseudo-elements in synchronization with loading progress. You can create a loop to show one step at a time and remove hidden class on each iteration. Be sure to add appropriate timing delay between steps for smooth animation effects.

8. Finally, make use of JavaScript code to handle loading sequence logic and control the appearance of these ASCII art images during runtime.

---

## User

write js functons too

Sure! Below is an example of JavaScript functions that can be used to control the loading sequence of the ASCII art preloader. This code will sequentially display different ASCII art images to simulate a terminal boot sequence.

```javascript
document.addEventListener("DOMContentLoaded", function() {
    const loadingSteps = [
        'logo-loading1.txt',
        'bar1.txt',
        'bar2.txt',
        'bar3.txt',
        'boot-complete.txt'
    ];
    let currentStep = 0;
    const preloaderContent = document.querySelector('.preloader-content');
    const loadingElements = preloaderContent.querySelectorAll('.loading1, .loading2');

    function showNextStep() {
        if (currentStep < loadingSteps.length) {
            // Hide all loading elements
            loadingElements.forEach(el => el.style.visibility = 'hidden');

            // Show the current loading step
            const currentLoadingElement = loadingElements[currentStep];
            currentLoadingElement.style.visibility = 'visible';

            // Update the content of the current loading element
            currentLoadingElement.innerHTML = `<pre>${fetchAsciiArt(loadingSteps[currentStep])}</pre>`;

            currentStep++;
            // Call the next step after a delay
            setTimeout(showNextStep, 1000); // Adjust delay as needed
        } else {
            // Loading complete, you can hide the preloader or show a message
            preloaderContent.innerHTML = '<pre>Boot Sequence Complete. Welcome!</pre>';
        }
    }
    function fetchAsciiArt(filePath) {
        // This function simulates fetching ASCII art from a file.
        // In a real implementation, you would use AJAX or Fetch API to get the content.
        const asciiArtMap = {
            'logo-loading1.txt': `
  ____  _            _       _
 |  _ \\| |          | |     | |
 | |_) | | ___   ___| | __ _| |_ ___  _ __
 |  _ <| |/ _ \\ / __| |/ _\` | __/ _ \\| '__|
 | |_) | | (_) | (__| | (_| | || (_) | |
 |____/|_|\\___/ \\___|_|\\__,_|\\__\\___/|_|
            `,
            'bar1.txt': `
[==========          ] 50%
            `,
            'bar2.txt': `
[================    ] 75%
            `,
            'bar3.txt': `
[====================] 100%
            `,
            'boot-complete.txt': `
Boot Sequence Complete. Welcome!
            `
        };
        return asciiArtMap[filePath] || '';
    }
    // Start the loading sequence
    showNextStep();
});
```

![alt text](image.png)

![alt text](image-1.png)
