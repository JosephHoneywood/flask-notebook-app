console.log('This is a test');

const notebookContainer = document.querySelector('[data-notebooks]');
const newNotebookForm = document.querySelector('[data-new-notebook-form]');
const newNotebookInput = document.querySelector('[data-new-notebook-input]');


const LOCAL_STORAGE_NOTEBOOK_KEY = 'chapter.notebook'
const LOCAL_STORAGE_SELECTED_NOTEBOOK_ID_KEY = 'chapter.selectedChapterId'

let notebooks = JSON.parse(localStorage.getItem(LOCAL_STORAGE_NOTEBOOK_KEY)) || [];
let selectedNotebookId = localStorage.getItem(LOCAL_STORAGE_SELECTED_NOTEBOOK_ID_KEY);

notebookContainer.addEventListener('click', e => {
    if (e.target.tagName.toLowerCase() === 'div') {
        selectedNotebookId = e.target.dataset.notebookId
        saveAndRender()
    };
});

newNotebookForm.addEventListener('submit', e => {
    e.preventDefault()
    const notebookName = newNotebookInput.value
    if (notebookName == null || notebookName === '') return
    const notebook = createNotebook(notebookName)
    newNotebookInput.value = null
    notebooks.push(notebook)
    console.log(notebooks)
    saveAndRender()
});

function createNotebook(name) {
    return { id: Date.now().toString(), name: name, chapters: [] }
};

function saveAndRender() {
    save()
    render()
};

function save() {
    localStorage.setItem(LOCAL_STORAGE_NOTEBOOK_KEY, JSON.stringify(notebooks));
    localStorage.setItem(LOCAL_STORAGE_SELECTED_NOTEBOOK_ID_KEY, selectedNotebookId);
};

function render() {
    clearElement(notebookContainer);
    console.log(notebooks)
    notebooks.forEach(notebook => {
        const divElement = document.createElement('div')
        divElement.dataset.notebookId = notebook.id
        divElement.classList.add('notebook', 'menu-item')
        divElement.innerText = notebook.name
        if (notebook.id === selectedNotebookId) {
            divElement.classList.add('active')
        };
        notebookContainer.appendChild(divElement)
    });
};

function clearElement(element) {
    while (element.firstChild) {
        element.removeChild(element.firstChild);
    };
};

render();

