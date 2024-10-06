document.getElementById('myForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Отменяем стандартное поведение формы

    const formData = new FormData(this);

    fetch("/submit/", {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,  // Передаем CSRF токен
        },
    })
    .then(response => {
        if (response.ok) {
            alert('Форма успешно отправлена!');
        } else {
            alert('Произошла ошибка при отправке формы');
        }
    })
    .catch(error => {
        console.error('Ошибка:', error);
        alert('Ошибка при подключении к серверу');
    });
});
