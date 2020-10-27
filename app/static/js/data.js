const notebook_container = document.querySelector('.notebooks');
const chapter_container = document.querySelector('.chapters')
const note_container = document.querySelector('.note-area')

let active_notebook = null;

// Find out what the user clicks in Notebooks
notebook_container.addEventListener('click', e => {
    if (e.target.tagName.toLowerCase() === 'div') {
        notebook_name = e.target.innerText
        console.log(notebook_name)
        active_notebook = notebook_name;
        get_chapters(notebook_name)
    };
});

// Find out what the user clicks in Chapters
chapter_container.addEventListener('click', e => {
    if (e.target.tagName.toLowerCase() === 'div') {
        chapter_name = e.target.innerText
        console.log(chapter_name)
        get_notes(chapter_name)
    };
})

function get_chapters(notebook_name) {
    //Get the chapters, triggered by a click on a notebook
    $.getJSON("/static/js/data_2.json", function(data){
        console.log(data)
        let chapters = data.filter(function(chapter){
            return chapter.name == notebook_name;
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

function get_notes(chapter_name) {
    //Get the notes, triggered by a click on a chapter
    $.getJSON("/static/js/data_2.json", function(data){
        let result = $.grep(data, function(v){
            return v.name == active_notebook;
        });
        chapters = result[0].content
        let result_c = $.grep(chapters, function(v){
            return v.chapter_name == chapter_name;
        });
        let result_n = result_c[0].chapter_contents;
        console.log(result_n);
        render_notes(result_n);
    });
};



// var found_names = $.grep(names, function(v) {
//     return v.name === "Joe" && v.age < 30;
// });

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

function render_notes(notes) {
    clearElement(note_container);
    notes.forEach(element => {

        //Create a new note element
        const divElement = document.createElement('div')
        divElement.classList.add('note')

        //Create a new note title area
        const divNoteTitleElement = document.createElement('div')
        divNoteTitleElement.classList.add('note-title-area')

        //Create a new note title
        const titleElement = document.createElement('h3')
        titleElement.classList.add('note-title')
        titleElement.innerText = element.title

        //Create a new edit button
        const editElement = document.createElement('button')
        editElement.classList.add('note-edit')
        editElement.innerText = 'Edit'

        //Create a HR
        const hrElement = document.createElement('hr')

        //Create a new body
        const bodyElement = document.createElement('p')
        bodyElement.classList.add('note-body')
        bodyElement.innerText = element.body

        //Create a new note footer area
        const footerElement = document.createElement('div')
        footerElement.classList.add('note-footer-area')

        //Create new tags
        const hashtagElement = document.createElement('div')
        hashtagElement.classList.add('note-tags')
        hashtagElement.innerText = String(element.tags)

        //Create new date
        const modifiedDateElement = document.createElement('div')
        modifiedDateElement.classList.add('note-date-info')
        modifiedDateElement.innerText = element.date_modified

        //Append footer children to their parent
        footerElement.append(hashtagElement, modifiedDateElement)

        //Append header children to their parent
        divNoteTitleElement.append(titleElement, editElement)

        //Append all elements to the note element
        divElement.append(divNoteTitleElement, hrElement, bodyElement, footerElement)

        note_container.appendChild(divElement)
    });
}



function clearElement(element) {
    while (element.firstChild) {
        element.removeChild(element.firstChild);
    };
};


// Start up function to load notebook names upon page load
$(document).ready(function(){
    $.getJSON("/static/js/data.json", function(data){
        let notebooks = [];
        // console.log(data);
        for (notebook in data) {
            notebooks.push(data[notebook].name);
        };
        // console.log(notebooks);
        render_notebooks(notebooks);
    }).fail(function(){
        console.log("An error has occurred.");
    });
});