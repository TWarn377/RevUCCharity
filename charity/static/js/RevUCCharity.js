function roundUp() {
  var amount = 1.35;
//  alert("hello");
  var amount = document.getElementById("inputDonation").value;
  var rounded = roundUp(amount, 0);
  var change = (rounded - amount).toFixed(2);
  alert(change);
  postData('http://ec2-18-235-225-4.compute-1.amazonaws.com:5000/api/donate', {
    change: change,
    timestamp: new Date().toISOString()});
}

function postData(url = ``, data = {}) {
  // Default options are marked with *
    return fetch(url, {
        method: "POST", // *GET, POST, PUT, DELETE, etc.
        mode: "no-cors", // no-cors, cors, *same-origin
        cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
        credentials: "same-origin", // include, *same-origin, omit
        headers: {
            "Content-Type": "application/json",
            // "Content-Type": "application/x-www-form-urlencoded",
        },
        redirect: "follow", // manual, *follow, error
        referrer: "no-referrer", // no-referrer, *client
        body: JSON.stringify(data), // body data type must match "Content-Type" header
    })
    .then(response => response.json()); // parses response to JSON
}

function subtract(aca = 0, rc = 0, achso = 0, sj = 0, maw = 0){

}
