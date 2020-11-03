const edit_btn = document.querySelector('.edit')
const delete_btn = document.querySelector('.delete')
const note_container = document.querySelector('.note-container')

const note_id = note_container.id;

edit_btn.addEventListener('click', e => {
    console.log('edit something')
});

delete_btn.addEventListener('click', e => {
    console.log('delete something')

    if (confirm("Are you sure you want to delete the note? This cant be reversed!")) {
        $.post( "/deletenote" , {
            id_to_del : note_id
        });
      };
});