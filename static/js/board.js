async function fetchData() {
    const response = await fetch('/api/getdata');
    const data = await response.json();
    const dataBoard = document.getElementById('data-board');
    if (data.contacts.length === 0) {
        dataBoard.innerHTML = '<img src="https://sun9-60.userapi.com/impf/c836734/v836734839/2f7b6/tk--hAjX7tQ.jpg?size=604x401&quality=96&sign=5159def6c804ce04bd9a8d057a002faa&type=album" alt="No contacts found" style="width: 100%; max-width: 604px;">';
    } else {
        dataBoard.textContent = JSON.stringify(data, null, 2);
    }
}
fetchData();
setInterval(fetchData, 5000);

document.getElementById('purge-button').addEventListener('click', function() {
    fetch('/api/purge', {
        method: 'GET'
    }).then(response => response.json())
      .then(data => {
          if (data.status === 'success') {
              console.log('Данные успешно очищены!');
          } else if (data.status === 'no_data') {
              console.log('Данных нет');
          } else {
              console.error('Ошибка: ' + data.message);
          }
      });
});
