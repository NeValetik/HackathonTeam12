document.addEventListener('DOMContentLoaded', () => {
  const searchBarInput = document.querySelector(".input-searchbar");
  const buttonSearch = document.querySelector(".search-button");

  console.log(buttonSearch);

  if (buttonSearch) {
    buttonSearch.addEventListener("click", async (e) => {
      console.log("click");
      const search = searchBarInput.value;
      chrome.runtime.sendMessage("OpenPopup")
      
    });
  }
});