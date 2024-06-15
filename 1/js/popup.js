document.addEventListener('DOMContentLoaded', () => {
  const searchBarInput = document.querySelector(".input-searchbar");
  const buttonSearch = document.querySelector(".search-button");

  if (buttonSearch) {
    buttonSearch.addEventListener("click", (e) => {
      const search = searchBarInput.value;
      chrome.runtime.sendMessage({request:"OpenPopup",message:search});
    });
  }
})