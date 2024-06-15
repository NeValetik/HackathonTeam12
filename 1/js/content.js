let intervalId
document.addEventListener('DOMContentLoaded', () => {
    const searchBarInput = document.querySelector(".input-searchbar");
    const buttonSearch = document.querySelector(".search-button");

    if (buttonSearch) {
        buttonSearch.addEventListener("click", (e) => {
        const search = searchBarInput.value;
        console.log("Sending message with search query:", search);  // Debug log
        chrome.runtime.sendMessage({ action: "OpenPopup", search: search }, (response) => {
            if (chrome.runtime.lastError) {
            console.error(chrome.runtime.lastError.message);
            } else {
            console.log("Response from background:", response);  // Debug log
            }
        });
        });
    }
});






