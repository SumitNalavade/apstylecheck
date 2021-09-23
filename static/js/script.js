function reset() {
    document.querySelector(".response-container").remove();
}

let logo = document.querySelector("#logo")
logo.addEventListener("click", (evt) => reset());

