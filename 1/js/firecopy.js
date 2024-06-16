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
<<<<<<< HEAD
            text_body.innerHTML = `
            <table class="content-table">
                <tr>
                <th><h3>Item</h3></th>
                <td><h3>${responseData.current_product.name}</h3></td>
                <td><h3>${responseData.similar_products['0'].name}</h3></td>
                <td><h3>${responseData.similar_products['1'].name}</h3></td>
                <td><h3>${responseData.similar_products['2'].name}</h3></td>
                </tr>
                <th><h3>Price</h3></th>
                <td>${responseData.current_product.details.price}</td>
                <td>$${responseData.similar_products['0'].price}</td>
                <td>$${responseData.similar_products['1'].price}</td>
                <td>$${responseData.similar_products['2'].price}</td>
                </tr>
                <tr>
                <th><h3>Battery</h3></th>
                <td>${responseData.current_product.details.scores.battery}</td>
                <td>${responseData.similar_products['0'].scores.battery}</td>
                <td>${responseData.similar_products['1'].scores.battery}</td>
                <td>${responseData.similar_products['2'].scores.battery}</td>
                </tr>
                <tr>
                <th><h3>Camera</h3></th>
                <td>${responseData.current_product.details.scores.camera}</td>
                <td>${responseData.similar_products['0'].scores.camera}</td>
                <td>${responseData.similar_products['1'].scores.camera}</td>
                <td>${responseData.similar_products['2'].scores.camera}</td>
                </tr>
                <tr>
                <th><h3>Overall</h3></th>
                <td>${responseData.current_product.details.scores.overall}</td>
                <td>${responseData.similar_products['0'].scores.overall}</td>
                <td>${responseData.similar_products['1'].scores.overall}</td>
                <td>${responseData.similar_products['2'].scores.overall}</td>
                </tr>
                <tr>
                <th><h3>Performance</h3></th>
                <td>${responseData.current_product.details.scores.performance}</td>
                <td>${responseData.similar_products['0'].scores.performance}</td>
                <td>${responseData.similar_products['1'].scores.performance}</td>
                <td>${responseData.similar_products['2'].scores.performance}</td>
                </tr>
                <tr>
                <th><h3>Quality</h3></th>
                <td>${responseData.current_product.details.scores.quality}</td>
                <td>${responseData.similar_products['0'].scores.quality}</td>
                <td>${responseData.similar_products['1'].scores.quality}</td>
                <td>${responseData.similar_products['2'].scores.quality}</td>
                </tr>
                <tr>
                <th><h3>Screen</h3></th>
                <td>${responseData.current_product.details.scores.screen}</td>
                <td>${responseData.similar_products['0'].scores.screen}</td>
                <td>${responseData.similar_products['1'].scores.screen}</td>
                <td>${responseData.similar_products['2'].scores.screen}</td>
                </tr>
                <tr>
                <th><h3>Value</h3></th>
                <td>${responseData.current_product.details.scores.value}</td>
                <td>${responseData.similar_products['0'].scores.value}</td>
                <td>${responseData.similar_products['1'].scores.value}</td>
                <td>${responseData.similar_products['2'].scores.value}</td>
                </tr>
                <tr>
                <th><h3>Link</h3></th>
                <td>-</td>
                <td><a href="${responseData.similar_products['0'].url}" target="_blank">Link 1</a></td>
                <td><a href="${responseData.similar_products['1'].url}" target="_blank">Link 2</a></td>
                <td><a href="${responseData.similar_products['2'].url}" target="_blank">Link 3</a></td>
                </tr>
            </table>
        `;
=======

            text_body.innerHTML = `<div>
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
            </div>`;

            let max_index = responseData.similar_products.length;
            for(let i = 0; i < max_index; i++){
                text_body.innerHTML += `<div class = "row">
            <h3> The tech: ${responseData.similar_products[String(i)].name}</h3>
                <h3> Price: ${responseData.similar_products[String(i)].price}</h3>
                <ul>
                <li> battery: ${responseData.similar_products[String(i)].scores.battery}</li>
                <li> camera: ${responseData.similar_products[String(i)].scores.camera}</li>
                <li> overall: ${responseData.similar_products[String(i)].scores.overall}</li>
                <li> performance: ${responseData.similar_products[String(i)].scores.performance}</li>
                <li> quality: ${responseData.similar_products[String(i)].scores.quality}</li>
                <li> screen: ${responseData.similar_products[String(i)].scores.screen}</li>
                <li> value: ${responseData.similar_products[String(i)].scores.value}</li>
                </ul>
            <a href="${responseData.similar_products[String(i)].url}" target="_blank">Url ${String(i+1)}</a>
            </div>`;
            }
>>>>>>> b3e565f218cda9459333d5a8cf23f3fe949d5b9d
        } catch (error) {
            console.error("Error sending request to the server:", error);
        }
    }
});