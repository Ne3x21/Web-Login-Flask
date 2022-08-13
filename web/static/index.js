function deleteNote(note_id) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ note_id: note_id }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function change() {
  document.getElementById('profile_inforamtion').style.display = 'none';
  document.getElementById('change_information').style.display = 'block';
}

function disable() {
  const cb = document.querySelector('#change_password');

  if(cb.checked == true) {
    document.getElementById('old_password').disabled = false;
    document.getElementById('new_password').disabled = false;
    document.getElementById('new_password_confirm').disabled = false;
  }
  else {
    document.getElementById('old_password').disabled = true;
    document.getElementById('new_password').disabled = true;
    document.getElementById('new_password_confirm').disabled = true;
  }
}

