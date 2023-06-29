function getData() {
    fetch('http://localhost:8000')
        .then(response => response.json())
        .then(data => {
            document.getElementById('data').textContent = data.message;
        })
        .catch(error => console.error(error));
}
