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
            name: request.message
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
            console.log(responseData);
            
            // Use the response data to update the text body
            const text_body = document.querySelector(".text-body");
            text_body.innerHTML = `
            <div>
                <h3> The tech: ${responseData.current_product.name}</h3>
                <h3> Price: ${responseData.current_product.details.price}</h3>
                <ul>
                <li> battery: ${responseData.current_product.details.scores.battery}</li>
                <li> camera: ${responseData.current_product.details.scores.camera}</li>
                <li> overall: ${responseData.current_product.details.scores.overall}</li>
                <li> performance: ${responseData.current_product.details.scores.performance}</li>
                <li> quality: ${responseData.current_product.details.scores.quality}</li>
                <li> screen: ${responseData.current_product.details.scores.screen}</li>
                <li> value: ${responseData.current_product.details.scores.value}</li>
                </ul>
            </div>
            <div class = "row">
            <h3> The tech: ${responseData.similar_products['0'].name}</h3>
                <h3> Price: ${responseData.similar_products['0'].price}</h3>
                <ul>
                <li> battery: ${responseData.similar_products['0'].scores.battery}</li>
                <li> camera: ${responseData.similar_products['0'].scores.camera}</li>
                <li> overall: ${responseData.similar_products['0'].scores.overall}</li>
                <li> performance: ${responseData.similar_products['0'].scores.performance}</li>
                <li> quality: ${responseData.similar_products['0'].scores.quality}</li>
                <li> screen: ${responseData.similar_products['0'].scores.screen}</li>
                <li> value: ${responseData.similar_products['0'].scores.value}</li>
                </ul>
            <a href="${responseData.similar_products['0'].url}" target="_blank">Url 1</a>
            </div>
            <div class = "row">
            <h3> The tech: ${responseData.similar_products['1'].name}</h3>
                <h3> Price: ${responseData.similar_products['1'].price}</h3>
                <ul>
                <li> battery: ${responseData.similar_products['1'].scores.battery}</li>
                <li> camera: ${responseData.similar_products['1'].scores.camera}</li>
                <li> overall: ${responseData.similar_products['1'].scores.overall}</li>
                <li> performance: ${responseData.similar_products['1'].scores.performance}</li>
                <li> quality: ${responseData.similar_products['1'].scores.quality}</li>
                <li> screen: ${responseData.similar_products['1'].scores.screen}</li>
                <li> value: ${responseData.similar_products['1'].scores.value}</li>
                </ul>
            <a href="${responseData.similar_products['1'].url}" target="_blank">Url 2</a>

            </div>
            <div class = "col">
            <h3> The tech: ${responseData.similar_products['2'].name}</h3>
                <h3> Price: ${responseData.similar_products['2'].price}</h3>
                <ul>
                <li> battery: ${responseData.similar_products['2'].scores.battery}</li>
                <li> camera: ${responseData.similar_products['2'].scores.camera}</li>
                <li> overall: ${responseData.similar_products['2'].scores.overall}</li>
                <li> performance: ${responseData.similar_products['2'].scores.performance}</li>
                <li> quality: ${responseData.similar_products['2'].scores.quality}</li>
                <li> screen: ${responseData.similar_products['2'].scores.screen}</li>
                <li> value: ${responseData.similar_products['2'].scores.value}</li>
                </ul>
                <a href= "${responseData.similar_products['2'].url}" target="_blank">Url 3</a>

            </div>         
            `;
        } catch (error) {
            console.error("Error sending request to the server:", error);
        }
    }
});