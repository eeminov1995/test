document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.btn-press');

    buttons.forEach(button => {
        button.addEventListener('touchstart', function() {
            button.classList.add('active');
        });

        button.addEventListener('touchend', function() {
            button.classList.remove('active');
        });

        button.addEventListener('touchcancel', function() {
            button.classList.remove('active');
        });
    });

    document.getElementById('data-form').addEventListener('submit', function(event) {
        event.preventDefault();
        const fio = document.getElementById('fio').value;
        const email = document.getElementById('email').value;
        const phone = document.getElementById('phone').value;
        const city = document.getElementById('city').value;

        fetch('/api/postdata', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ fio: fio, email: email, phone: phone, city: city })
        }).then(response => response.json())
          .then(data => {
              if (data.status === 'success') {
                  console.log('Данные успешно добавлены!');
                  document.getElementById('fio').value = '';
                  document.getElementById('email').value = '';
                  document.getElementById('phone').value = '';
                  document.getElementById('city').value = '';
                  fetchData(); // Обновляем данные после добавления
              } else {
                  console.error('Ошибка: ' + data.message);
              }
          });
    });

    document.getElementById('test-button').addEventListener('click', function() {
        fetch('/api/addtestdata', {
            method: 'POST'
        }).then(response => response.json())
          .then(data => {
              if (data.status === 'success') {
                  console.log('Тестовые данные успешно добавлены!');
                  fetchData(); // Обновляем данные после добавления
              } else {
                  console.error('Ошибка: ' + data.message);
              }
          });
    });

    document.getElementById('purge-button').addEventListener('click', function() {
        fetch('/api/purge', {
            method: 'GET'
        }).then(response => response.json())
          .then(data => {
              if (data.status === 'success') {
                  console.log('Данные успешно очищены!');
                  fetchData(); // Обновляем данные после очистки
              } else if (data.status === 'no_data') {
                  console.log('Данных нет');
              } else {
                  console.error('Ошибка: ' + data.message);
              }
          });
    });

    function fetchData() {
        fetch('/api/getdata')
            .then(response => response.json())
            .then(data => {
                const contactsList = document.getElementById('contacts-list');
                contactsList.innerHTML = ''; // Очищаем текущий список контактов
                if (data.contacts.length === 0) {
                    const noContactsItem = document.createElement('li');
                    noContactsItem.className = 'list-group-item text-center';
                    noContactsItem.textContent = 'Нет контактов';
                    contactsList.appendChild(noContactsItem);
                } else {
                    data.contacts.forEach(contact => {
                        const contactItem = document.createElement('li');
                        contactItem.className = 'list-group-item';
                        contactItem.innerHTML = `
                            <h5 class="mb-1">${contact.fio}</h5>
                            <p class="mb-1">Email: ${contact.email}</p>
                            <p class="mb-1">Телефон: ${contact.phone}</p>
                            <p class="mb-1">Город: ${contact.city}</p>
                        `;
                        contactsList.appendChild(contactItem);
                    });
                }
            });
    }

    fetchData(); // Первоначальная загрузка данных
});
