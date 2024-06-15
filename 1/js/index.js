// document.addEventListener('DOMContentLoaded', async () => {
//     const response = await fetch('D:/chrome_extension/1/js/data.json');
//     const data = await response.json();

//     const text_body = document.querySelector(".text-body");

//     text_body.innerHTML = `
//         <h3>${data.Telefon.name}</h3>
//     `;
// });


chrome.runtime.onMessage.addListener(async (request) => {
    if (request.request == "findIt"){
        console.log("Received search query:", request.message);
        const text_body = document.querySelector(".text-body");

        text_body.innerHTML = `
            <h3>${request.message}</h3>
        `;
    }
})