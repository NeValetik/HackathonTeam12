
chrome.runtime.onInstalled.addListener(async () => {
  let url = chrome.runtime.getURL("html/hello.html");
  let tab = await chrome.tabs.create({ url });

  chrome.storage.sync.get(['showClock'], (result) => {
    if (result.showClock) {
      chrome.action.setBadgeText({ text: 'ON' });
    }
  });

  chrome.storage.sync.get(['timer'], (result) => {
    console.log('result', result)
    if (!result.timer) {
      chrome.storage.sync.set({ 'timer': 1 })
    }
  });
});

chrome.runtime.onMessage.addListener(async (request) => {
	console.log("Received search query:", request.message);
  	if (request.request == "OpenPopup") {
      	chrome.windows.create({
          	url: "/html/index.html",
			type: "popup",
			focused: true,
			width: 400,
			height: 600,
			top: 0,
      	}, () => {
          console.log(request.message)
		})
  	}
})

