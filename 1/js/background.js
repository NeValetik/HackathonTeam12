// background.js

chrome.runtime.onMessage.addListener(async (request) => {
    console.log("Received search query:", request.message);
    if (request.request == "OpenPopup") {
        chrome.tabs.create({
            url: "/html/index.html",
            active: true,
        }, (tab) => {
            chrome.tabs.onUpdated.addListener(function listener(tabId, changeInfo) {
                if (tabId === tab.id && changeInfo.status === 'complete') {
                  chrome.tabs.onUpdated.removeListener(listener);
                  // Send message to the new tab
                  chrome.tabs.sendMessage(tabId, { request: "findIt", message: request.message });
                }
              });
        });
    }
});

var funcToInject = function() {
    var selection = window.getSelection();
    return (selection.rangeCount > 0) ? selection.toString() : '';
};

chrome.commands.onCommand.addListener(function(cmd) {
    if (cmd == 'find-the-comparison') {
        chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
            var activeTab = tabs[0];
            chrome.scripting.executeScript(
                {
                    target: { tabId: activeTab.id, allFrames: true },
                    func: funcToInject
                },
                function(results) {
                    if (chrome.runtime.lastError) {
                        console.log('ERROR:\n' + chrome.runtime.lastError.message);
                    } else if (results.length > 0 && typeof results[0].result === 'string') {
                        console.log('Selected text: ' + results[0].result);
                        chrome.tabs.create({
                            url: "/html/index.html",
                            active: true,
                        }, (tab) => {
                            console.log(results[0].result);
                            // Wait for the new tab to fully load
                            chrome.tabs.onUpdated.addListener(function listener(tabId, info) {
                                if (info.status === 'complete' && tabId === tab.id) {
                                    chrome.tabs.onUpdated.removeListener(listener);
                                    // Send message to the new tab
                                    chrome.tabs.sendMessage(tabId, {request: "findIt", message: results[0].result});
                                }
                            });
                        });
                    }
                }
            );
        });
    }
});

// Create context menu item on extension installation
chrome.runtime.onInstalled.addListener(function() {
    chrome.contextMenus.create({
      title: "Open with Button",
      contexts: ["selection"],
      id: "openWithButton"
    });
  });
  
  // Handle clicks on the context menu item
  chrome.contextMenus.onClicked.addListener(function(info, tab) {
    if (info.menuItemId === "openWithButton") {
      let selectedWord = info.selectionText.trim();
      if (selectedWord !== "") {
        chrome.tabs.create({
          url: "/html/index.html",
          active: true,
        }, function(newTab) {
          // Wait for the new tab to fully load
          chrome.tabs.onUpdated.addListener(function listener(tabId, changeInfo) {
            if (tabId === newTab.id && changeInfo.status === 'complete') {
              chrome.tabs.onUpdated.removeListener(listener);
              // Send message to the new tab
              chrome.tabs.sendMessage(tabId, { request: "findIt", message: selectedWord });
            }
          });
        });
      }
    }
  });
  
  


// async function fetchData() {
//     try {
//         const response = await fetch('http://127.0.0.1:5000/api/data');
//         if (!response.ok) {
//             throw new Error('Network response was not ok');
//         }
//         const data = await response.json();
//         document.getElementById('data').textContent = JSON.stringify(data);
//     } catch (error) {
//         console.error('There has been a problem with your fetch operation:', error);
//     }
// }