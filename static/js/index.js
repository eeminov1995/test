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
          } else {
              console.error('Ошибка: ' + data.message);
          }
      });
});
