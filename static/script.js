function clear() {
  for(let i of document.querySelectorAll(".response-text-container")) {
    i.remove();
  }
}

document.querySelector("#logo").addEventListener("click", (evt) => clear());
