const notebook_container = document.querySelector('.notebooks');
const chapter_container = document.querySelector('.chapters')
const note_container = document.querySelector('.note-area')

//Find out what the user clicks in Notebooks
notebook_container.addEventListener('click', e => {
    if (e.target.tagName.toLowerCase() === 'div') {
        notebook_name = e.target.innerText
        console.log(notebook_name)
        $.post( "/_getchapters", {
            send_notebook_name : notebook_name
        }).done(function( data ){
            render_chapters(data)
        });
    };
});

// Find out what the user clicks in Chapters
chapter_container.addEventListener('click', e => {
    if (e.target.tagName.toLowerCase() === 'div') {
        chapter_name = e.target.innerText
        console.log(chapter_name)
        $.post( "/_getnotes", {
            send_chapter_name : chapter_name
        }).done(function( data ){
            console.log(data)
            console.log(JSON.parse(data))
            render_notes(JSON.parse(data))
        });
    };
})

// Find out if a user has clicked a note
note_container.addEventListener('click', e => {
    console.log(e.target.className)
    if (e.target.className === 'note-title') {
        console.log(e.target.id)
        note_id = e.target.id
        window.location.href = `/displaynote/${note_id}`
    };
});

// function get_chapters(notebook_name) {
//     //Get the chapters, triggered by a click on a notebook
//     $.getJSON("/static/js/data_2.json", function(data){
//         console.log(data)
//         let chapters = data.filter(function(chapter){
//             return chapter.name == notebook_name;
//         });
//         chapters = chapters[0].content;
//         let chapter_names = [];
//         for (chapter in chapters) {
//             chapter_names.push(chapters[chapter].chapter_name);
//         };
//         console.log(chapter_names);
//         render_chapters(chapter_names);
//     });
// };

// Render all chapters
function render_chapters(chapters) {
    clearElement(chapter_container);
    array_chapters = chapters.split(",")
    array_chapters.forEach(element => {
        const divElement = document.createElement('div')
        divElement.classList.add('chapter', 'menu-item')
        divElement.innerText = element
        chapter_container.appendChild(divElement)
    });
};

//Render all notes
function render_notes(notes) {
    clearElement(note_container);
    notes.forEach(element => {

        //Create a new note element
        const divElement = document.createElement('div')
        divElement.classList.add('note')

        //Create a new note title area
        const divNoteTitleElement = document.createElement('div')
        divNoteTitleElement.classList.add('note-title-area')
        
        //Create a new note title and attach the mongoID reference
        const titleElement = document.createElement('h3')
        titleElement.classList.add('note-title')
        titleElement.innerText = element['note_title']
        titleElement.id = element['_id']['$oid']

        //Create a HR
        const hrElement = document.createElement('hr')

        //Create a new body
        const bodyElement = document.createElement('p')
        bodyElement.classList.add('note-body')
        bodyElement.innerHTML = element['note_body']

        //Create a new note footer area
        const footerElement = document.createElement('div')
        footerElement.classList.add('note-footer-area')

        //Create new tags
        const hashtagElement = document.createElement('div')
        hashtagElement.classList.add('note-tags')
        hashtagElement.innerText = String(element['note_tags'])

        //Create new date
        const modifiedDateElement = document.createElement('div')
        modifiedDateElement.classList.add('note-date-info')
        modifiedDateElement.innerText = element['note_created_date']

        //Append footer children to their parent
        footerElement.append(hashtagElement, modifiedDateElement)

        //Append header children to their parent
        divNoteTitleElement.append(titleElement)

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