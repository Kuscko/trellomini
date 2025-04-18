// kanban.js
let draggedTaskId = null;

function handleDragStart(event) {
  draggedTaskId = event.target.getAttribute("data-task-id");
}

function handleDrop(event) {
  event.preventDefault();
  const newStatus = event.currentTarget.getAttribute("data-status");

  const projectPk = document.getElementById("kanban-board").getAttribute("data-project-pk");
  fetch(`/projects/${projectPk}/tasks/${draggedTaskId}/status/${newStatus}/`, {
    method: 'POST',
    headers: {
      'X-CSRFToken': getCookie('csrftoken'),
    },
  })
  .then(response => {
    if (response.ok) {
      location.reload();
    } else {
      alert("Failed to update task status.");
    }
  });
}

// Util to get CSRF token from cookie
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}
