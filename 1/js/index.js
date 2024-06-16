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
        
        // Define the server URL
        const serverUrl = "http://localhost:5000/findIt"; // Adjust the URL according to your Flask server configuration
        
        // Create the payload
        const payload = {
            message: request.message
        };
        
        try {
            // Send the POST request to the Flask server
            const response = await fetch(serverUrl, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(payload)
            });
            
            // Parse the response as JSON
            const responseData = await response.json();
            
            // Use the response data to update the text body
            const text_body = document.querySelector(".text-body");
            text_body.innerHTML = `
                <h3>${responseData.responseMessage}</h3>
            `;
        } catch (error) {
            console.error("Error sending request to the server:", error);
        }
    }
});