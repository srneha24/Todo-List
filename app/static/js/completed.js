function completed_status(checkbox, id) {    
    var checkbox = document.getElementById("completed".concat(id));
    var status;

    if (checkbox.checked) {
        status = 1;
    }
    else {
        status = 0;
    }
    
    var completed = {
        id: checkbox.value,
        status: status
    };

    console.log(completed);

    fetch(`/`, {
        method: "PUT",
        credentials: "include",
        body: JSON.stringify(completed),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    })
}