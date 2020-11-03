const edit_btn = document.querySelector('.edit');
const delete_btn = document.querySelector('.delete');
const save_btn = document.querySelector('.save');
const note_container = document.querySelector('.note-container');
const note_text = document.querySelector('.text-content');

const note_id = note_container.id;

edit_btn.addEventListener('click', e => {
    console.log('I am edit and I was clicked')

    edit_btn.classList.toggle('hide')
    save_btn.classList.toggle('hide')

    note_text.setAttribute('contenteditable', "true")
    note_text.focus()
    note_text.style.backgroundColor = "#DCDCDC"  

});

save_btn.addEventListener('click', e => {
    console.log('I am save and I was clicked')
    save_updated_note()
    
    save_btn.classList.toggle('hide')
    edit_btn.classList.toggle('hide')

    note_text.style.backgroundColor = 'whitesmoke'
    note_text.setAttribute('contenteditable', 'false')
    note_text.blur()

});


delete_btn.addEventListener('click', e => {
    console.log('delete something')

    if (confirm("Are you sure you want to delete the note? This cant be reversed!")) {
        $.post( "/deletenote" , {
            id_to_del : note_id
        });
      };
});


function save_updated_note() {
    console.log('Time to save!')
    console.log(`Updating ${note_id}`)
    let note_body = note_text.innerText
    $.post( "/updatenote", {
        id_to_upd : note_id,
        updated_content : note_body
    });
};