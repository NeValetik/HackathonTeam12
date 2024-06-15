chrome.runtime.onMessage.addListener(async (request) => {
	console.log("Received search query:", request.message);
  	if (request.request == "OpenPopup") {
		chrome.tabs.create({
			url: "/html/index.html",
			active: true,
		  }, (tab) => {
			console.log(tab);
		  });
  	}
})

