function searchBooks() {
    const searchInput = document.getElementById('searchInput').value;
    alert(`Você pesquisou por: ${searchInput}`);
    // Aqui você pode adicionar a lógica de busca, como fazer uma requisição para um servidor
}

function goToUserArea() {
    window.location.href = 'user_area.html';
}

function goToHome() {
    window.location.href = 'index.html';
}

function goToCatalogo() {
    window.location.href = 'catalogo.html';
}

let count = 1;
document.getElementById("radio1").checked = true;

setInterval( function(){
    nextImage();
}, 2000)

function nextImage(){
    count++;
    if(count>4){
        count= 1;
    }
    document.getElementById("radio"+count).checked = true;

}