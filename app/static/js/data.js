const notebook_container = document.querySelector('.notebooks');
const chapter_container = document.querySelector('.chapters')

// Find out what the user clicker in Notebooks
notebook_container.addEventListener('click', e => {
    if (e.target.tagName.toLowerCase() === 'div') {
        notebook_name = e.target.innerText
        console.log(notebook_name)
        get_chapters(notebook_name)
    };
});

function get_chapters(notebook_name) {
    $.getJSON("/static/js/data.json", function(data){
        // console.log(data.notebooks);
        let chapters = data.notebooks.filter(function(notebook){
            return notebook.name == notebook_name;
        });
        chapters = chapters[0].content;
        let chapter_names = [];
        for (chapter in chapters) {
            chapter_names.push(chapters[chapter].chapter_name);
        };
        console.log(chapter_names);
        render_chapters(chapter_names);
    });
};


// Render all Notebooks function to run on page load
function render_notebooks(notebooks) {
    notebooks.forEach(element => {
        const divElement = document.createElement('div')
        divElement.classList.add('notebook', 'menu-item')
        divElement.innerText = element
        notebook_container.appendChild(divElement)
    });
};

function render_chapters(chapters) {
    clearElement(chapter_container);
    chapters.forEach(element => {
        const divElement = document.createElement('div')
        divElement.classList.add('chapter', 'menu-item')
        divElement.innerText = element
        chapter_container.appendChild(divElement)
    });
};

function clearElement(element) {
    while (element.firstChild) {
        element.removeChild(element.firstChild);
    };
};


// Start up function to load notebook names upon page load
$(document).ready(function(){
    $.getJSON("/static/js/data.json", function(data){
        let notebooks = [];
        for (notebook in data.notebooks) {
            notebooks.push(data.notebooks[notebook].name)
        };
        render_notebooks(notebooks);
    }).fail(function(){
        console.log("An error has occurred.");
    });
});