const edit_btn = document.querySelector('.edit');
const delete_btn = document.querySelector('.delete');
const save_btn = document.querySelector('.save');
const note_container = document.querySelector('.note-container');
const note_text = document.querySelector('.text-content');

const note_id = note_container.id;

let edit = function() {
    $('.note-body').summernote(
        {focus: true,
         maxwidth: 500,
         height: 500,
         maxheight: 500
        });
    edit_btn.classList.toggle('hide')
    save_btn.classList.toggle('hide')
  };
  
let save = function() {
    let markup = $('.note-body').summernote('code');
    $('.note-body').summernote('destroy');
    save_updated_note(markup);
    edit_btn.classList.toggle('hide')
    save_btn.classList.toggle('hide')
  };


delete_btn.addEventListener('click', e => {
    console.log('delete something')

    if (confirm("Are you sure you want to delete the note? This cant be reversed!")) {
        $.post( "/deletenote" , {
            id_to_del : note_id
        }).done(
            window.location.href = `/index`
        );
      };
});


function save_updated_note(markup) {
    console.log('Time to save!')
    console.log(`Updating ${note_id}`)
    $.post( "/updatenote", {
        id_to_upd : note_id,
        updated_content : markup
    });
};