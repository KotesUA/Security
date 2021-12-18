function getCredentials() {
    return {
        email: document.getElementById("email").value,
        password: document.getElementById("password").value
    };
}

function postData(url, data, callback) {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = () => {if (xhr.readyState === 4) callback(xhr);};
    xhr.open("post", url);
    xhr.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
    xhr.send(JSON.stringify(data));
}

document.getElementById("register").addEventListener("click", () => {
    let data = getCredentials();
    postData("/register", data, xhr => alert(xhr.response));
});

document.getElementById("login").addEventListener("click", () => {
    let data = getCredentials();
    postData("/login", data, xhr => alert(xhr.response));
});